from cx_Freeze import setup, Executable

target = Executable(
    script="Main.py",
    base="Win32GUI",
    icon="image\icon.ico",
    target_name="ASL.exe")

setup(
    name="Velvet",
    version="1.0",
    options={"build_exe":  {"packages": ["pygame", "mediapipe", "cv2", "pywin32"],
                            "include_files": ["songs", "games", "SuperLegendBoy.ttf", "image"]}},
    executables=[target])

# python thucthi.py build
