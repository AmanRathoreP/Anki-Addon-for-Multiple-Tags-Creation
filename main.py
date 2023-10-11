from aqt.qt import QAction
from aqt.utils import qconnect
from aqt import mw
from .src import my_logger, my_user_interactive_GUI

my_logger.add_log("all stuff imported")


def show_custom_dialog() -> dict:
    dialog = my_user_interactive_GUI.MyCustomDialog(mw)
    dialog.exec_()
    return dialog.get_files_info()


def create_multiple_tags() -> None:
    # TODO while logging the info the dict of info is printing two times. Perhaps something is running multiple times fix it
    info = show_custom_dialog()
    mw.showWarning("One or multiple tags were not created") if (__create_tags(__get_tag_names(
        info["deliminator"], info["files"])) == False) else print('')



def __create_tags(tags: list) -> bool:
    """Create tags from the list provide with 
    Returns True if tags are successfully created
    Returns False if tags are not created successfully"""
    # TODO add functionality to work it with anki's backend
    pass


def __get_tag_names(deliminator: str, file_paths: list) -> list:
    """Create list of the tags from the files path and deliminator provided
    Returns list of the tags"""
    tags = set()
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as f:
                tags.update(f.read().split(deliminator))
        except Exception as e:
            my_logger.add_log(
                "Probably the file is non readable", my_logger.logging.ERROR)
            my_logger.add_log(e, my_logger.logging.ERROR)
    return [item for item in list(tags) if item.strip()]

action = QAction("Create Multiple Tags", mw)
qconnect(action.triggered, create_multiple_tags)
mw.form.menuTools.addAction(action)
