import quest
import VS
import vsrandom
import Base
import Director
import mission_lib

activelinks=[]
activeobjs=[]
def checkSaveValue (playernum,questname, value):
    return quest.checkSaveValue(playernum,questname,value)
def setSaveValue (playernum,name,value):
	quest.removeQuest(playernum,name,value);

def payCheck(playernum,savevalue,value,money):
    if checkSaveValue(playernum,savevalue,value):
        VS.getPlayerX(playernum).addCredits(money)
        setSaveValue(playernum,savevalue,value+1)

class Choice:
	def __init__(self,pics,actions,name):
		self.pics=pics
		self.name=name
		self.actions=actions
	def Draw(self,room,x,y,wid,hei):
		Base.Texture(room,self.name,self.pics,x+(wid/2),y+(wid/2))
		Base.Python(room,self.name,x,y,wid,hei,self.name,self.actions,True)
		activelinks.append((room,self.name))
		activeobjs.append((room,self.name))
class Fixer:
	def __init__(self,name,text,precondition,image,choices):
		self.name = name
		self.text = text
		self.precondition = precondition
		self.image = image
		self.choices = choices
	def abletodraw(self):
		for cond in self.precondition:
			var= cond[0]
			value = cond[1]
			if not checkSaveValue(VS.getCurrentPlayer(),var,value):
				return False
			
		return True
	def drawobjs(self,room,x,y,wid,hei):
		Base.Texture(room,self.name,self.image,x+(wid/2),y+(hei/2))
		Base.Python(room,self.name,x,y,wid,hei,self.text,self.choices,True)

class RandFixer (Fixer):
	def __init__ (self,which):
		fixer=mission_lib.CreateRandomMission(which)
		Fixer.__init__(self,fixer[1].split(' ')[-1].lower(),fixer[1],[],fixer[0],"bases/fixers/generic%d.py"%which)

fixers={"enigma_sector/niven":[
	Fixer("explore","Talk to the Explorer",[("enigma_sector/enigma_nav",0)],"bases/fixers/militia.spr","bases/fixers/explore_enigma.py"),
	Fixer("explore","Talk to the Explorer",[("enigma_sector/enigma_nav",3),("gemini_sector/delta_navpoint",0),("gemini_sector/beta_navpoint",0)],"bases/fixers/militia.spr","bases/fixers/explore_notready.py"),
	Fixer("explore","Talk to the Explorer",[("enigma_sector/enigma_nav",3),("gemini_sector/delta_navpoint",1),("gemini_sector/beta_navpoint",0)],"bases/fixers/militia.spr","bases/fixers/explore_beta.py"),
	Fixer("explore","Talk to the Explorer",[("enigma_sector/enigma_nav",3),("gemini_sector/delta_navpoint",2),("gemini_sector/beta_navpoint",0)],"bases/fixers/militia.spr","bases/fixers/explore_beta.py"),
	Fixer("explore","Talk to the Explorer",[("enigma_sector/enigma_nav",3),("gemini_sector/delta_navpoint",2),("gemini_sector/beta_navpoint",1),("gemini_sector/gamma_navpoint",0)],"bases/fixers/militia.spr","bases/fixers/explore_gamma.py"),
	Fixer("explore","Talk to the Explorer",[("enigma_sector/enigma_nav",3),("gemini_sector/delta_navpoint",2),("gemini_sector/beta_navpoint",2),("gemini_sector/gamma_navpoint",0)],"bases/fixers/militia.spr","bases/fixers/explore_gamma.py"),
	Fixer("explore","Talk to the Explorer",[("enigma_sector/enigma_nav",3),("gemini_sector/delta_navpoint",2),("gemini_sector/beta_navpoint",2),("gemini_sector/gamma_navpoint",1),("gemini_sector/delta_prime_navpoint",0)],"bases/fixers/militia.spr","bases/fixers/explore_delta_prime.py"),
	Fixer("explore","Talk to the Explorer",[("enigma_sector/enigma_nav",3),("gemini_sector/delta_navpoint",2),("gemini_sector/beta_navpoint",2),("gemini_sector/gamma_navpoint",2),("gemini_sector/delta_prime_navpoint",0)],"bases/fixers/militia.spr","bases/fixers/explore_delta_prime.py"),
	Fixer("explore","Talk to the Explorer",[("enigma_sector/enigma_nav",3),("gemini_sector/delta_navpoint",2),("gemini_sector/beta_navpoint",2),("gemini_sector/gamma_navpoint",2),("gemini_sector/delta_prime_navpoint",1)],"bases/fixers/militia.spr","bases/fixers/attack_drone0.py"),
	],"enigma_sector/enigma":[
	Fixer("confed_drone","Talk to the Confed Officer",[("quest_drone",1)],"bases/fixers/confed.spr","bases/fixers/attack_drone1.py"),
	Fixer("confed_drone","Talk to the Confed Officer",[("quest_drone",-1)],"bases/fixers/confed.spr","bases/fixers/attack_drone1.py")
	],"enigma_sector/heinlein":[
	Fixer ("cloaked_man","Speak with hooded figure",[("decided_iso_good",0)],"bases/fixers/cloak.spr","bases/fixers/iso_antagonist.py"),
	Fixer ("rowenna","Speak with Rowenna",[("decided_iso_evil",0),("iso_mission2",0)],"bases/fixers/iso.spr","bases/fixers/iso.py"),
	Fixer ("rowenna","Speak with Rowenna",[("decided_iso_evil",0),("iso_mission2",-1)],"bases/fixers/iso.spr","bases/fixers/iso.py")
	],"enigma_sector/adams":[
	Fixer ("rowenna","Speak with Rowenna",[("decided_iso_evil",0),("iso_mission3",0),("iso_mission2",1)],"bases/fixers/iso.spr","bases/fixers/iso.py"),
	Fixer ("rowenna","Speak with Rowenna",[("decided_iso_evil",0),("iso_mission3",0),("iso_mission2",-1)],"bases/fixers/iso.spr","bases/fixers/iso.py"),
	Fixer ("cloaked_man","Speak with hooded figure",[("decided_iso_good",0),("iso_evil2",1)],"bases/fixers/cloak.spr","bases/fixers/iso_antagonist.py")
	],"enigma_sector/defiance":[
	Fixer ("rowenna","Speak with Rowenna",[("decided_iso_evil",0),("iso_mission3",1)],"bases/fixers/iso.spr","bases/fixers/iso.py"),
	Fixer ("rowenna","Speak with Rowenna",[("decided_iso_evil",0),("iso_mission3",-1)],"bases/fixers/iso.spr","bases/fixers/iso.py")
	],"enigma_sector/blake":[
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission1",-1)],"bases/fixers/pirate.spr","bases/fixers/pirates.py"),
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission1",0)],"bases/fixers/pirate.spr","bases/fixers/pirates.py"),
	],"enigma_sector/rigel":[
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission1",-1)],"bases/fixers/pirate.spr","bases/fixers/pirates.py"),
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission2",-1)],"bases/fixers/pirate.spr","bases/fixers/pirates.py"),
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission3",-1)],"bases/fixers/pirate.spr","bases/fixers/pirates.py"),
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission4",-1)],"bases/fixers/pirate.spr","bases/fixers/pirates.py"),
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission1",0)],"bases/fixers/pirate.spr","bases/fixers/pirates.py"),
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission1",1),("pirate_mission2",0)],"bases/fixers/pirate.spr","bases/fixers/pirates.py"),
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission1",1),("pirate_mission2",1),("pirate_mission3",2),("pirate_mission4",0)],"bases/fixers/pirate.spr","bases/fixers/pirates.py"),
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission1",1),("pirate_mission2",1),("pirate_mission3",2),("pirate_mission4",1)],"bases/fixers/pirate.spr","bases/fixers/pirates.py"),
	],"sol_sector/tingvallir":[
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission1",-1)],"bases/fixers/pirate.spr","bases/fixers/pirates.py"),
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission2",-1)],"bases/fixers/pirate.spr","bases/fixers/pirates.py"),
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission3",-1)],"bases/fixers/pirate.spr","bases/fixers/pirates.py"),
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission1",1),("pirate_mission2",0)],"bases/fixers/pirate.spr","bases/fixers/pirates.py"),
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission1",1),("pirate_mission2",1),("pirate_mission3",0)],"bases/fixers/pirate.spr","bases/fixers/pirates.py"),
	Fixer ("pirate","Talk with the Pirate",[("pirate_mission1",1),("pirate_mission2",1),("pirate_mission3",1),("pirate_mission4",0)],"bases/fixers/pirate.spr","bases/fixers/pirates.py")
	]}


def AppendFixer(name,fixer):
	fixers[name]=fixer

def DestroyActiveButtons ():
	for button in activelinks:
		Base.EraseLink(button[0],button[1])
	for button in activeobjs:
		Base.EraseObj(button[0],button[1])
def CreateChoiceButtons (room,buttonlist,vert=False,spacing=.025,wid=.2,hei=.2):
	x=0
	if (vert):
		x=-(wid/2)
		y=-((hei*len(buttonlist)*spacing)+spacing)/2
	else:
		y=-.75-(hei/2)
		x=-(wid*len(buttonlist)+(len(buttonlist)-1)*spacing)/2
	print x,y
	for button in buttonlist:
		button.Draw(room,x,y,wid,hei)
		if (vert):
			y-=(spacing+hei)
		else:
			x+=spacing+wid
		
def CreateFixers (room,locations):
	fixerlist = fixers.get (VS.getSystemFile())
	j=0
	if (fixerlist):
		for i in range (len(fixerlist)):
			if (j<len(locations) and fixerlist[i].abletodraw()):
				fixerlist[i].drawobjs (room,locations[j][0],locations[j][1],locations[j][2],locations[j][3])
				j+=1
	rndnum=vsrandom.random()
	if rndnum<.1 and j==0:
		f=RandFixer(0)
		f.drawobjs (room,locations[j][0],locations[j][1],locations[j][2],locations[j][3])
		j+=1
		img=f.image
		rndnum=vsrandom.random()
		if rndnum<.75:
			i=0
			while f.image==img and i<10:
				f=RandFixer(1)
				i+=1
			if i<10:
				f.drawobjs (room,locations[j][0],locations[j][1],locations[j][2],locations[j][3])
				j+=1
