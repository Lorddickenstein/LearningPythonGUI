#DearPyGUI Imports
import dearpygui.dearpygui as dpg

# window object settings
dpg.create_context()
dpg.create_viewport(title='DearPyGui', width=540, height=720)
dpg.set_global_font_scale(1.25)
dpg.add_theme()

with dpg.window(label='Simple SMS Spam Filter', width=520, height=677):
    print("GUI is running...")
    dpg.set_item_pos("Simple SMS Spam Filter", [0, 0])

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()