from graphviz import Digraph
# Skapa UML Aktivitetsdiagram
uml_activity = Digraph("UML_Activity_Diagram", format="png")
uml_activity.attr(rankdir="TB")
uml_activity.attr('node', shape='ellipse')

# Skapa noder för aktivitetsdiagrammet
uml_activity.node("Start", "Start", shape="circle", style="filled", fillcolor="green")
uml_activity.node("FyllInfo", "Fyll i användaruppgifter")
uml_activity.node("Validera", "Validera information")
uml_activity.node("SkapaKonto", "Skapa konto")
uml_activity.node("SkickaMail", "Skicka bekräftelsemail")
uml_activity.node("Slut", "Slut", shape="circle", style="filled", fillcolor="red")

# Skapa kanter för att binda noderna i diagrammet
uml_activity.edge("Start", "FyllInfo")
uml_activity.edge("FyllInfo", "Validera")
uml_activity.edge("Validera", "SkapaKonto", label="Validering OK")
uml_activity.edge("Validera", "FyllInfo", label="Validering ej OK", style="dashed")
uml_activity.edge("SkapaKonto", "SkickaMail")
uml_activity.edge("SkickaMail", "Slut")

# Spara diagrammet till fil
uml_activity.render("/mnt/data/UML_Activity_Diagram_New.png", cleanup=True)