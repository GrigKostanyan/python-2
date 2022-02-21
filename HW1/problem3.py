class Button:
  def __init__(self):
    pass

class WinButton(Button):
  def __init__(self):
    print("WinButton")

class MacButton(Button):
  def __init__(self):
    print("MacButton")

class Checkbox:
  def __init__(self):
    pass

class WinCheckbox(Checkbox):
  def __init__(self):
    print("WinCheckbox")

class MacCheckbox(Checkbox):
  def __init__(self):
    print("MacCheckbox")

class GUIFactory:
  def createButton(self):
    pass
  def createCheckbox(self):
    pass

class WinFactory(GUIFactory):
  def createButton(self):
    return WinButton()

  def createCheckbox(self):
    return WinCheckbox()

class MacFactory(GUIFactory):
  def createButton(self):
    return MacButton()

  def createCheckbox(self):
    return MacCheckbox()

class Application:
  def __init__(self):
    factories = { "1": WinFactory,
                  "2": MacFactory }
    os = input("Choose OS:\n1 - Win\n2 - Mac\n")
    if os in factories:
      self.factory = factories[os]()
    else:
      print("Invalid number...")
      self.factory = GUIFactory()

  def createUI(self):
    self.factory.createButton()
    self.factory.createCheckbox()

  def paint(self):
    print("paint...")

a = Application()
a.createUI()
a.paint()
