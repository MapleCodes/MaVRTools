"""
Time Wasted: 4hrs
"""

import TIER.trifork as TRIFORK # You won't have this one.
import functions_env as FB
import functions_vr as FVR
import functions_controller as FC
import initialization as MINIT

import dotenv, os
import customtkinter as ctk


### GLOBAL VARIABLES ###
FONT = "Segoe SD"
SIDE_BUTTON_FDATA = f"{FONT}", 12, "bold"

### END GLOBAL VARIABLES ###


### MAIN WINDOW ###
app = ctk.CTk()  
app.geometry("1280x720")
app.title("Malunette")
# app.iconbitmap("TEST.ico")

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue") 

### END MAIN WINDOW ###


### INLINE FUNCTIONS ###
def LP_SWITCH_DELETEENV_FUNCTION():
    if LP_SWITCH_VAR.get() == "off":
        LP_BUTTON_DELETEENV.configure(state="disabled")
    elif LP_SWITCH_VAR.get() == "on":
        LP_BUTTON_DELETEENV.configure(state="normal")

### END INLINE FUNCTIONS ###


### INLINE VARIABLES ###
LP_SWITCH_VAR = ctk.StringVar(value="off")

### END INLINE VARIABLES ###


### LEFT PANEL ###
app.grid_rowconfigure(0, weight=1)

LEFT_PANEL = ctk.CTkFrame(app, width=300, corner_radius=0)
LEFT_PANEL.grid(column=0, row=0, rowspan=10 , sticky="nsew")
LEFT_PANEL.grid_rowconfigure(10, weight=1)

LP_LABEL_FRONTER = ctk.CTkLabel(LEFT_PANEL, text="$ Malunette", font=(f"{FONT}", 35, "bold"))
LP_LABEL_FRONTER.grid(column=0, row=0, padx=20, pady=(35, 35))

LP_BUTTON_DISCORD = ctk.CTkButton(LEFT_PANEL, text="DISCORD TOKEN", font=SIDE_BUTTON_FDATA, command=FB.dotENVDiscordBot)
LP_BUTTON_DISCORD.grid(column=0, row=1, padx=20, pady=(0, 20), ipadx=25, ipady=7)

LP_BUTTON_OPENAI = ctk.CTkButton(LEFT_PANEL, text="OPENAI TOKEN", font=SIDE_BUTTON_FDATA, command=FB.dotENVOpenAI)
LP_BUTTON_OPENAI.grid(column=0, row=2, padx=20, pady=(0, 20), ipadx=25, ipady=7)

LP_BUTTON_WEBCAPTIONER = ctk.CTkButton(LEFT_PANEL, font=SIDE_BUTTON_FDATA, text="WEBCAPTIONER")
LP_BUTTON_WEBCAPTIONER.grid(column=0, row=3, padx=20, pady=(0, 20), ipadx=25, ipady=7)

LP_BUTTON_TRIFORK = ctk.CTkButton(LEFT_PANEL, text="TRIFORK KEY", font=SIDE_BUTTON_FDATA, command=FB.dotENVTriFork)
LP_BUTTON_TRIFORK.grid(column=0, row=4, padx=20, pady=(0, 20), ipadx=25, ipady=7)

LP_SWITCH_DELETEENV = ctk.CTkSwitch(LEFT_PANEL, text="Enable Delete", font=SIDE_BUTTON_FDATA, command=LP_SWITCH_DELETEENV_FUNCTION, variable=LP_SWITCH_VAR, onvalue="on", offvalue="off")
LP_SWITCH_DELETEENV.grid(column=0, row=11, padx=(0, 75), pady=(0, 20))

LP_BUTTON_DELETEENV = ctk.CTkButton(LEFT_PANEL, text="DELETE .ENV CONFIG", font=SIDE_BUTTON_FDATA, command=FB.dotENVDelete, fg_color="#ab1b25", hover_color="#8c1119")
LP_BUTTON_DELETEENV.grid(column=0, row=12, padx=20, pady=(0, 20), ipadx=25, ipady=7)

LP_BUTTON_START = ctk.CTkButton(LEFT_PANEL, text="START ALL", font=SIDE_BUTTON_FDATA, command=FVR.TriForkDecryption, fg_color="#1e9400", hover_color="#236912")
LP_BUTTON_START.grid(column=0, row=13, padx=20, pady=(0, 20), ipadx=25, ipady=7)

### END LEFT PANEL ###


### MAIN APP ###
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=0)
app.grid_rowconfigure(1, weight=1)

MA_LABEL_TOP = ctk.CTkLabel(app, text="GENERAL OUTPUT / INPUT DISPLAY", font=(f"{FONT}", 20, "bold"))
MA_LABEL_TOP.grid(column=1, row=0, padx=20, pady=(20, 0), sticky="w")

MAIN_TABVIEW = ctk.CTkTabview(app)
MAIN_TABVIEW.grid(column=1, row=1, padx=20, pady=(0, 20), sticky="nsew")
MAIN_TABVIEW.add("Discord")
MAIN_TABVIEW.add("WebCaptioner")
MAIN_TABVIEW.add("TriFork")

#region Discord TABVIEW
DISCTAB_CANVAS = ctk.CTkCanvas(MAIN_TABVIEW.tab("Discord"))


#endregion


### END MAIN APP ###


### START CONFIG ###
LP_BUTTON_WEBCAPTIONER.configure(state="disabled")
LP_BUTTON_TRIFORK.configure(state="disabled")
LP_BUTTON_DELETEENV.configure(state="disabled")

### END START CONFIG ###


### BEGIN ###
MINIT.fts()
app.mainloop()
### END BEGIN ###