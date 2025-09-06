import random
from xoxxox.shared import Custom, LibLog

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
    self.conlog = LibLog.getlog(diccnf["conlog"]) # PRM
    self.conlog.catsys(diccnf) # PRM

  def infere(self, txtreq):
    prompt = self.conlog.catreq(txtreq) # PRM
    print("prompt[" + prompt + "]", flush=True) # DBG
    keytxt = txtreq
    try:
      t = self.dictxt[keytxt]
    except:
      keytxt = next(iter(self.dictxt))
    if self.postxt[keytxt] >= len(self.dictxt[keytxt]):
      self.postxt[keytxt] = 0
      if self.output == "random":
        random.shuffle(self.dictxt[keytxt])
    txtifr = self.dictxt[keytxt][self.postxt[keytxt]]
    print("txtifr[" + txtifr + "]", flush=True) # DBG
    txtres, txtana = self.conlog.arrres(txtifr) # PRM
    print("txtres[" + txtres + "]", flush=True) # DBG
    print("txtana[" + txtana + "]", flush=True) # DBG
    self.conlog.catres(txtres) # PRM
    self.postxt[keytxt] = self.postxt[keytxt] + 1
    return txtres
