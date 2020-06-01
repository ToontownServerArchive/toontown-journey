from panda3d.core import *
from direct.gui.DirectGui import *
from direct.gui import DirectGuiGlobals
from direct.showbase.DirectObject import DirectObject
from otp.avatar import Avatar

class ChatHistory(DirectFrame, DirectObject):

    def __init__(self):
        DirectFrame.__init__(self, relief = None, sortOrder = 500)
        DirectObject.__init__(self)
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')

        self.history = DirectScrolledList(parent = self, decButton_pos = (0.45, 0, 0.65), decButton_image = (gui.find('**/FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), decButton_relief = None, incButton_pos = (0.45, 0, -0.1475), incButton_image= (gui.find('**//FndsLst_ScrollUp'), gui.find('**/FndsLst_ScrollDN'), gui.find('**/FndsLst_ScrollUp_Rllvr'), gui.find('**/FndsLst_ScrollUp')), incButton_relief = None, incButton_scale = (1.0, 1.0, -1.0), itemFrame_geom = (loader.loadModel('phase_3.5/models/gui/frame')), itemFrame_geom_scale = (0.14, 1, 0.17), itemFrame_geom_pos = (0, 0, -0.25), itemFrame_geom_color=(1,1,1, 0.6), itemFrame_relief = None, items = [], numItemsVisible = 6, forceHeight = 0.1, itemFrame_frameSize = (-0.4, 0.5, -0.4, 0.16), itemFrame_pos = (0.45, 0, 0.5))
        self.isHidden = True
        base.cr.chatHistory = self 

    def stop(self):
        self.history.destroy()
        base.cr.chatHistory = None 
    def addToHistory(self, msg, av_id=0):
        msg = msg.replace('\n', ' ')
        msgDirectButton = DirectButton(relief = None, text = msg, text_scale =0.035, text_pos = (-0.44, 0), text_style=3,text_align=TextNode.ALeft, text_wordwrap=25, text_shadow=(0, 0, 0, 1), command=self.buttonizeIt, extraArgs = [av_id])
        self.history.addItem(msgDirectButton)
        self.history.scrollTo(len(self.history['items']) - 1)

    def toggle(self):
        if self.isHidden:
            self.posInterval(0.5, Point3(0.12, 0, 0.2), blendType = 'easeInOut').start()
            self.isHidden = False
            base.setCellsActive([base.leftCells[0]], 0)
        else:
            self.posInterval(0.5, Point3(-1, 0, 0.2), blendType = 'easeInOut').start()
            self.isHidden = True
            base.setCellsActive([base.leftCells[0]], 1)

    def updateTransparency(self, transparency):
        self.history.itemFrame_geom_color[3] = transparency

    def buttonizeIt(self, av_id):
        av = base.cr.doId2do.get(av_id)
        if not av:
            return
        if str(av_id)[:2] != '10':
            return
        av.clickedNametag()



    