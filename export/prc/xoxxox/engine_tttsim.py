import random
from xoxxox.shared import Custom

#---------------------------------------------------------------------------

class TttPrc:

  def __init__(self, config="xoxxox/config_tttsim_000", **dicprm):
    diccnf = Custom.update(config, dicprm)
    self.dictxt = {}
    self.postxt = {}

  def status(self, config="xoxxox/config_tttsim_000", **dicprm):
    diccnf = Custom.update(config, dicprm)
    if self.dictxt != diccnf["dictxt"]:
      self.dictxt = diccnf["dictxt"]
      self.output = diccnf["output"]
      for keytxt in self.dictxt.keys():
        self.postxt[keytxt] = 0
        if self.output == "random":
          random.shuffle(self.dictxt[keytxt])

  def infere(self, txtreq):
    keytxt = txtreq
    try:
      t = self.dictxt[keytxt]
    except:
      keytxt = next(iter(self.dictxt))
    if self.postxt[keytxt] >= len(self.dictxt[keytxt]):
      self.postxt[keytxt] = 0
      if self.output == "random":
        random.shuffle(self.dictxt[keytxt])
    txtres = self.dictxt[keytxt][self.postxt[keytxt]]
    self.postxt[keytxt] = self.postxt[keytxt] + 1
    return txtres
