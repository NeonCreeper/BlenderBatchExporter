#Tell blender the metadata of the add-on
bl_info = {
    "name": "Animation Batch Exporter",
    "description": "Exports a batch file that renders the scene as an animation using the windows command line to the same directory as the currently opened blend file", 
    "category": "Import-Export",
    "author": "Nate Townsend", 
    "version": (0,1),
}
import bpy
import os

class exportbatchfile(bpy.types.Operator):
    """Exports a batch that renders the scene with the CMD"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "export.batch_export"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Export Animation Batch File"         # Display name in the interface.
    
    def execute(self, context):
        
        #Write Blender EXE's directory to a variable and print it, without the blender.exe at the end
        exepath = bpy.app.binary_path
        bfolderpath = exepath.replace('blender.exe','')
        print(bfolderpath)
        #Print the blend file's path
        if bpy.data.is_saved == True:
            filepath = bpy.data.filepath
            blendfilename = os.path.basename(filepath)
            blendfilefolder = os.path.dirname(filepath)
            fullblendpath = "%s\%s" % (blendfilefolder, blendfilename)
            print(fullblendpath)
        else:
            print("Blend file has not yet been saved")
            self.report({'ERROR'}, 'Blend file has not yet been saved - you need to save you project before you can run this script!') 
        #Write the batch file that will start the render
        batch = open(os.path.join(blendfilefolder, 'render.bat'), 'a+')
        batch.write("""cd %s
        blender -b "%s" -a""" % (bfolderpath, fullblendpath))
        batch.close()
        return {'FINISHED'}

def register():
    bpy.utils.register_class(exportbatchfile)


def unregister():
    bpy.utils.unregister_class(exportbatchfile)