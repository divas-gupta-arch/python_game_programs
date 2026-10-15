import re
from datetime import datetime
from pathlib import Path

import streamlit as st

# ---------------------------------------------------------------- config
BASE_DIR = Path("workspace")
BASE_DIR.mkdir(exist_ok=True)

st.set_page_config(page_title="FileVault | File Manager", page_icon="📁", layout="wide")

# ---------------------------------------------------------------- styling
st.markdown(
    """
<style>
    .block-container {padding-top: 2rem; max-width: 1100px;}
    .hero {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #db2777 100%);
        padding: 2rem 2.2rem; border-radius: 18px; color: white; margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(79,70,229,.25);
    }
    .hero h1 {margin: 0; font-size: 2.1rem; font-weight: 800; letter-spacing: -.5px;}
    .hero p {margin: .4rem 0 0; opacity: .9; font-size: 1.02rem;}
    .card {
        background: rgba(124,58,237,.07); border: 1px solid rgba(124,58,237,.22);
        border-radius: 14px; padding: 1.1rem 1.3rem; text-align: center;
    }
    .card .num {font-size: 1.9rem; font-weight: 800; color: #7c3aed;}
    .card .lbl {font-size: .85rem; opacity: .75; text-transform: uppercase; letter-spacing: .08em;}
    div.stButton > button, div.stDownloadButton > button, div[data-testid="stFormSubmitButton"] > button {
        border-radius: 10px; font-weight: 600; padding: .55rem 1.2rem;
    }
    div[data-testid="stSidebar"] {border-right: 1px solid rgba(124,58,237,.2);}
    .footer {text-align:center; opacity:.55; font-size:.85rem; margin-top:2.5rem;}
</style>
""",
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------- helpers
def safe_path(name: str) -> Path:
    """Return a path inside BASE_DIR. Blocks empty names, folders and '..'."""
    name = name.strip()
    if not name:
        raise ValueError("File name cannot be empty.")
    if name in {".", ".."} or Path(name).name != name:
        raise ValueError("Use a plain file name (no folders or '..').")
    if not re.fullmatch(r"[\w\-. ]+", name):
        raise ValueError("Use only letters, numbers, spaces, '_', '-' and '.'.")
    return BASE_DIR / name


def list_files():
    files = [p for p in BASE_DIR.iterdir() if p.is_file()]
    return sorted(files, key=lambda p: p.stat().st_mtime, reverse=True)


def human_size(n: int) -> str:
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.0f} {unit}" if unit == "B" else f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def flash(kind: str, msg: str):
    st.session_state["flash"] = (kind, msg)


def create_file(name: str, data: str):
    path = safe_path(name)
    if path.exists():
        raise FileExistsError("A file with this name already exists.")
    path.write_text(data, encoding="utf-8")


def read_file(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def append_file(path: Path, data: str):
    existing = read_file(path)
    sep = "" if (not existing or existing.endswith("\n")) else "\n"
    with open(path, "a", encoding="utf-8") as fs:
        fs.write(sep + data)


def overwrite_file(path: Path, data: str):
    path.write_text(data, encoding="utf-8")


def rename_file(path: Path, new_name: str):
    new_path = safe_path(new_name)
    if new_path.exists():
        raise FileExistsError("A file with the new name already exists.")
    path.rename(new_path)


def delete_file(path: Path):
    path.unlink()


# ---------------------------------------------------------------- flash messages
if "flash" in st.session_state:
    kind, msg = st.session_state.pop("flash")
    st.toast(msg, icon="✅" if kind == "success" else "⚠️")

# ---------------------------------------------------------------- sidebar
files = list_files()
file_names = [f.name for f in files]

with st.sidebar:
    st.markdown("## 📁 FileVault")
    st.caption("Create · Read · Update · Delete")
    page = st.radio(
        "Navigate",
        ["🏠 Dashboard", "➕ Create", "📖 Read", "✏️ Update", "🗑️ Delete"],
        label_visibility="collapsed",
    )
    st.divider()
    st.caption(f"**{len(files)}** file(s) in workspace")
    for n in file_names[:8]:
        st.markdown(f"- `{n}`")
    if len(file_names) > 8:
        st.caption(f"+ {len(file_names) - 8} more")

# ---------------------------------------------------------------- hero
st.markdown(
    """
<div class="hero">
    <h1>📁 FileVault</h1>
    <p>A clean file manager built with Python &amp; Streamlit. Create, read, edit and delete files in one place.</p>
</div>
""",
    unsafe_allow_html=True,
)


def need_files() -> bool:
    if not file_names:
        st.info("No files yet. Go to **➕ Create** and make your first one.")
        return False
    return True


# ---------------------------------------------------------------- pages
if page == "🏠 Dashboard":
    total_size = sum(f.stat().st_size for f in files)
    last = (
        datetime.fromtimestamp(files[0].stat().st_mtime).strftime("%d %b, %H:%M")
        if files
        else "-"
    )
    c1, c2, c3 = st.columns(3)
    for col, num, lbl in [
        (c1, len(files), "Total files"),
        (c2, human_size(total_size), "Total size"),
        (c3, last, "Last modified"),
    ]:
        col.markdown(
            f'<div class="card"><div class="num">{num}</div><div class="lbl">{lbl}</div></div>',
            unsafe_allow_html=True,
        )

    st.markdown("### Your files")
    if files:
        st.dataframe(
            [
                {
                    "Name": f.name,
                    "Size": human_size(f.stat().st_size),
                    "Modified": datetime.fromtimestamp(f.stat().st_mtime).strftime(
                        "%Y-%m-%d %H:%M"
                    ),
                }
                for f in files
            ],
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("Your workspace is empty. Create a file to get started.")

elif page == "➕ Create":
    st.markdown("### Create a new file")
    with st.form("create_form", clear_on_submit=True):
        name = st.text_input("File name", placeholder="notes.txt")
        data = st.text_area("Content", height=250, placeholder="Write something...")
        submitted = st.form_submit_button("Create file", type="primary")
    if submitted:
        try:
            create_file(name, data)
            flash("success", f"'{name.strip()}' created successfully.")
            st.rerun()
        except Exception as err:
            st.error(str(err))

elif page == "📖 Read":
    st.markdown("### Read a file")
    if need_files():
        choice = st.selectbox("Choose a file", file_names)
        path = safe_path(choice)
        content = read_file(path)
        st.caption(
            f"{human_size(path.stat().st_size)} · {len(content.splitlines())} line(s)"
        )
        st.code(content if content else "(empty file)", language=None)
        st.download_button("⬇️ Download", content, file_name=choice)

elif page == "✏️ Update":
    st.markdown("### Update a file")
    if need_files():
        choice = st.selectbox("Choose a file", file_names)
        path = safe_path(choice)
        op = st.radio("Operation", ["Append", "Overwrite", "Rename"], horizontal=True)

        if op == "Append":
            with st.form("append_form", clear_on_submit=True):
                data = st.text_area("Text to add at the end", height=180)
                if st.form_submit_button("Append", type="primary"):
                    append_file(path, data)
                    flash("success", f"Appended to '{choice}'.")
                    st.rerun()

        elif op == "Overwrite":
            with st.form("overwrite_form"):
                data = st.text_area(
                    "New content (replaces everything)",
                    value=read_file(path),
                    height=260,
                )
                if st.form_submit_button("Overwrite", type="primary"):
                    overwrite_file(path, data)
                    flash("success", f"'{choice}' overwritten.")
                    st.rerun()

        else:
            with st.form("rename_form"):
                new_name = st.text_input("New file name", value=choice)
                if st.form_submit_button("Rename", type="primary"):
                    try:
                        rename_file(path, new_name)
                        flash("success", f"Renamed to '{new_name.strip()}'.")
                        st.rerun()
                    except Exception as err:
                        st.error(str(err))

elif page == "🗑️ Delete":
    st.markdown("### Delete a file")
    if need_files():
        choice = st.selectbox("Choose a file", file_names)
        st.warning(f"This will permanently delete **{choice}**.")
        confirm = st.checkbox("Yes, I'm sure")
        if st.button("Delete file", type="primary", disabled=not confirm):
            delete_file(safe_path(choice))
            flash("success", f"'{choice}' deleted.")
            st.rerun()

st.markdown(
    '<div class="footer">Built with Python &amp; Streamlit · Files are stored in the <code>workspace/</code> folder</div>',
    unsafe_allow_html=True,
)

