import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from numpy import sin, cos, pi, linspace



df = pd.read_excel('C:\\Users\\Helen laptop\\Documents\\Gaitrite_ST_graphs\\AXNB 14 Feb 2023 Initial Ax.xlsx')
#print(df)

Left_Cadence = df.loc[4,'Cadence']
Left_Walking_Speed = (df.loc[4,'Velocity'])/100
#Left_Stride_Time =
#Left_Step_Time =
Left_Single_Support = df.loc[4,'Single Supp. Time(sec) L']
Left_Double_Support = df.loc[4,'Double Supp. Time(sec) L']
Left_Stride_Length = (df.loc[4,'Stride Length(cm) L'])/100
Left_Step_Length = (df.loc[4,'Step Length(cm) L'])/100
Left_Step_Width = (df.loc[4,'HH Base Support (cm) L'])/100
Left_Foot_progression=  df.loc[4,'Foot progression L']

Right_Cadence = df.loc[4,'Cadence']
Right_Walking_Speed = (df.loc[4,'Velocity'])/100
#Right_Stride_Time = df.loc[4,'Velocity']
#Right_Step_Time = df.loc[4,'Velocity']
Right_Single_Support = df.loc[4,'Single Supp. Time(sec) R']
Right_Double_Support = df.loc[4,'Double Supp. Time(sec) R']
Right_Stride_Length = (df.loc[4,'Stride Length(cm) R'])/100
Right_Step_Length = (df.loc[4,'Step Length(cm) R'])/100
Right_Step_Width = (df.loc[4,'HH Base Support (cm) R'])/100
Right_Foot_progression=  df.loc[4,'Foot progression R']

Both_Cadence = (Right_Cadence + Left_Cadence)/2
Both_Walking_Speed = ((Right_Walking_Speed + Left_Walking_Speed)/2)
#Both_Stride_Time =
#Both_Step_Time =
Both_Single_Support = (Right_Single_Support + Left_Single_Support)/2
Both_Double_Support = (Right_Double_Support + Left_Double_Support)/2
Both_Stride_Length = ((Right_Stride_Length + Left_Stride_Length)/2)
Both_Step_Length = ((Right_Step_Length + Left_Step_Length)/2)
Both_Step_Width = ((Right_Step_Width + Left_Step_Width)/2)
Both_Foot_progression = (Right_Foot_progression + Left_Foot_progression)/2

Left_Cadence_SD = df.loc[5,'Cadence']
Left_Walking_Speed_SD = (df.loc[5,'Velocity'])/100
#Left_Stride_Time_SD = df.loc[5,'Velocity']
#Left_Step_Time_SD = df.loc[5,'Velocity']
Left_Single_Support_SD = df.loc[5,'Single Supp. Time(sec) L']
Left_Double_Support_SD = df.loc[5,'Double Supp. Time(sec) L']
Left_Stride_Length_SD = (df.loc[5,'Stride Length(cm) L'])/100
Left_Step_Length_SD = (df.loc[5,'Step Length(cm) L'])/100
Left_Step_Width_SD = (df.loc[5,'HH Base Support (cm) L'])/100
Left_Foot_progression_SD = df.loc[5,'Foot progression L']

Right_Cadence_SD = df.loc[5,'Cadence']
Right_Walking_Speed_SD = (df.loc[5,'Velocity'])/100
#Right_Stride_Time_SD = df.loc[5,'Velocity']
#Right_Step_Time_SD = df.loc[5,'Velocity']
Right_Single_Support_SD = df.loc[5,'Single Supp. Time(sec) R']
Right_Double_Support_SD = df.loc[5,'Double Supp. Time(sec) R']
Right_Stride_Length_SD = (df.loc[5,'Stride Length(cm) R'])/100
Right_Step_Length_SD = (df.loc[5,'Step Length(cm) R'])/100
Right_Step_Width_SD = (df.loc[5,'HH Base Support (cm) R'])/100
Right_Foot_progression_SD = df.loc[5,'Foot progression R']

Both_Cadence_SD = (Right_Cadence_SD + Left_Cadence_SD)/2
Both_Walking_Speed_SD = ((Right_Walking_Speed_SD + Left_Walking_Speed_SD)/2)
#Both_Stride_Time_SD =
#Both_Step_Time_SD =
Both_Single_Support_SD = (Right_Single_Support_SD + Left_Single_Support_SD)/2
Both_Double_Support_SD = (Right_Double_Support_SD + Left_Double_Support_SD)/2
Both_Stride_Length_SD = ((Right_Stride_Length_SD + Left_Stride_Length_SD)/2)
Both_Step_Length_SD = ((Right_Step_Length_SD + Left_Step_Length_SD)/2)
Both_Step_Width_SD = ((Right_Step_Width_SD + Left_Step_Width_SD)/2)
Both_Foot_progression_SD = (Right_Foot_progression_SD + Left_Foot_progression_SD)/2

#Normal Cadence
NCadence = 113
NCadenceB = int((Both_Cadence/NCadence)*100)
NCadenceL = int((Left_Cadence/NCadence)*100)
NCadenceR = int((Right_Cadence/NCadence)*100)

#Normal Walking Speed
NWS = 1.38
NWSB = int((Both_Walking_Speed/NWS)*100)
NWSL = int((Left_Walking_Speed/NWS)*100)
NWSR = int((Right_Walking_Speed/NWS)*100)

#Normal Stride time
NStrT = 0
#NStrT%B
#NStrT%L
#NStrT%R
#Normal Step time
NStepT = 0
#NStepT%B
#NStepT%L
#NStepT%R
#Normal Single Support
NSS = 0.42
SSB = int((Both_Single_Support/NSS)*100)
SSL = int((Left_Single_Support/NSS)*100)
SSR = int((Right_Single_Support/NSS)*100)
#Normal double support
NDS = 0.23
DSB = int((Both_Double_Support/NDS)*100)
DSL = int((Left_Double_Support/NDS)*100)
DSR = int((Right_Double_Support/NDS)*100)
#Normal stride length
NStrL = 1.44
StrLB = int((Both_Stride_Length/NStrL)*100)
StrLL = int((Left_Stride_Length/NStrL)*100)
StrLR = int((Right_Stride_Length/NStrL)*100)
#Normal step length
NStepL = 0.72
SLB = int((Both_Step_Length/NStepL)*100)
SLL = int((Left_Step_Length/NStepL)*100)
SLR = int((Right_Step_Length/NStepL)*100)
#Normal step width
NStepW = 0.2
SWB = int((Both_Step_Width/NStepW)*100)
SWL = int((Left_Step_Width/NStepW)*100)
SWR = int((Right_Step_Width/NStepW)*100)
#Normal stance phase
#NSTPh = 60.73
#StPhB =
#StPhL =
#StPhR =

fig, axs = plt.subplots(4, 2, figsize=(8, 9.5))

plt.subplots_adjust(left=0.10,
                    bottom=0.05,
                    right=0.90,
                    top=0.95,
                    wspace=0.4,
                    hspace=0.4)
i = 0
x = []
x = ["Normal", "L&R", "Left", "Right"]
colors = ['green','orange','red','blue']

velsd = [0.25, Both_Walking_Speed_SD, Left_Walking_Speed_SD, Right_Walking_Speed_SD]
veldata = [NWS, round(Both_Walking_Speed,2), round(Left_Walking_Speed,2), round(Right_Walking_Speed,2)]
veldata_ = [NWS/2, Both_Walking_Speed/2, Left_Walking_Speed/2, Right_Walking_Speed/2]
velref = [100, NWSB, NWSL, NWSR]
velref_ = [str(100) + "%", str(NWSB) + "%", str(NWSL) + "%", str(NWSR) + "%"]
axs[0, 0].set_title('Walking Velocity', fontsize=10)
axs[0, 0].tick_params(axis='x', labelsize=10)
axs[0, 0].tick_params(axis='y', labelsize=8)
axs[0, 0].set_ylabel('m/s', fontsize=8)
axs[0, 0].bar(x, veldata, color= colors, yerr= velsd)
for i, v in enumerate(veldata):
    axs[0, 0].text(i - 0.40, veldata[i], veldata[i], fontsize=7, color="gray", fontweight='bold')
for i, v in enumerate(velref):
    axs[0, 0].text(i - 0.38, veldata_[i], velref_[i], fontsize=10, color="white", fontweight='bold')

caddata = [113, round(Both_Cadence,2), round(Left_Cadence,2), round(Right_Cadence,2)]
caddata_ = [113/2, Both_Cadence/2, Left_Cadence/2, Right_Cadence/2]
ebc = [5, Both_Cadence_SD, Left_Cadence_SD, Right_Cadence_SD]
cadref = [100, NCadenceB,NCadenceL,NCadenceR]
cadref_ = [str(100) + "%", str(NCadenceB) + "%", str(NCadenceL) + "%", str(NCadenceR) + "%"]
axs[0, 1].set_title('Cadence', fontsize=10)
axs[0, 1].tick_params(axis='x', labelsize=10)
axs[0, 1].tick_params(axis='y', labelsize=8)
axs[0, 1].set_ylabel('steps/min', fontsize=8)
axs[0, 1].bar(x, caddata, color=colors, yerr=ebc)
for i, v in enumerate(caddata):
    axs[0, 1].text(i - 0.40, caddata[i], caddata[i], fontsize=7, color="gray", fontweight='bold')
for i, v in enumerate(cadref):
    axs[0, 1].text(i - 0.38, caddata_[i], cadref_[i], fontsize=10, color="white", fontweight='bold')

sldata = [0.72, round(Both_Step_Length,2), round(Left_Step_Length,2), round(Right_Step_Length,2)]
sldata_ = [0.72/2, Both_Step_Length/2, Left_Step_Length/2, Right_Step_Length/2]
ebsl = [0.1, Both_Step_Length_SD, Left_Step_Length_SD, Right_Step_Length_SD]
slref = [100, SLB, SLL, SLR]
slref_ = [str(100) + "%", str(SLB) + "%", str(SLL) + "%", str(SLR) + "%"]
axs[1, 0].set_title('Step Length', fontsize=10)
axs[1, 0].tick_params(axis='x', labelsize=10)
axs[1, 0].tick_params(axis='y', labelsize=8)
axs[1, 0].set_ylabel('m', fontsize=8)
axs[1, 0].bar(x, sldata, color= colors, yerr=ebsl)
for i, v in enumerate(sldata):
    axs[1, 0].text(i - 0.40, sldata[i], sldata[i], fontsize=7, color="gray", fontweight='bold')
for i, v in enumerate(slref):
    axs[1, 0].text(i - 0.38, sldata_[i], slref_[i], fontsize=10, color="white", fontweight='bold')
#here
stldata = [1.44, round(Both_Stride_Length,2), round(Left_Stride_Length,2), round(Right_Stride_Length,2)]
stldata_ =[1.44/2, Both_Stride_Length/2, Left_Stride_Length/2, Right_Stride_Length/2]
errstl = [0.2, Both_Stride_Length_SD, Left_Stride_Length_SD, Right_Stride_Length_SD]
stlref = [100, StrLB, StrLL, StrLR]
stlref_ = [str(100) + "%", str(StrLB) + "%", str(StrLL) + "%", str(StrLR) + "%"]
axs[1, 1].set_title('Stride Length', fontsize=10)
axs[1, 1].tick_params(axis='x', labelsize=10)
axs[1, 1].tick_params(axis='y', labelsize=8)
axs[1, 1].set_ylabel('m', fontsize=8)
axs[1, 1].bar(x, stldata, color= colors, yerr=errstl)
for i, v in enumerate(stldata):
    axs[1, 1].text(i - 0.40, stldata[i], stldata[i], fontsize=7, color="gray", fontweight='bold')
for i, v in enumerate(stlref):
    axs[1, 1].text(i - 0.38, stldata_[i], stlref_[i], fontsize=10, color="white", fontweight='bold')

ssdata = [0.42, round(Both_Single_Support,2), round(Left_Single_Support,2), round(Right_Single_Support,2)]
ssdata_ = [0.42/2, Both_Single_Support/2, Left_Single_Support/2, Right_Single_Support/2]
errss = [0.05, Both_Single_Support_SD, Left_Single_Support_SD, Right_Single_Support_SD]
ssref = [100, SSB, SSL, SSR]
ssref_ = [str(100) + "%", str(SSB) + "%", str(SSL) + "%", str(SSR) + "%"]
axs[2, 0].set_title('Single Support', fontsize=10)
axs[2, 0].tick_params(axis='x', labelsize=10)
axs[2, 0].tick_params(axis='y', labelsize=8)
axs[2, 0].set_ylabel('s', fontsize=8)
axs[2, 0].bar(x, ssdata, color = colors, yerr = errss)
for i, v in enumerate(ssdata):
    axs[2, 0].text(i - 0.40, ssdata[i], ssdata[i], fontsize=7, color="gray", fontweight='bold')
for i, v in enumerate(ssref):
    axs[2, 0].text(i - 0.38, ssdata_[i], ssref_[i], fontsize=10, color="white", fontweight='bold')

dsdata = [0.23, round(Both_Double_Support,2), round(Left_Double_Support,2), round(Right_Double_Support,2)]
dsdata_ = [0.23/2, Both_Double_Support/2, Left_Double_Support/2, Right_Double_Support/2]
errds = [0.01, Both_Double_Support_SD, Left_Double_Support_SD, Right_Double_Support_SD]
dsref = [100, DSB, DSL, DSR]
dsref_ = [str(100) + "%", str(DSB) + "%", str(DSL) + "%", str(DSR) + "%"]
axs[2, 1].set_title('Double Support', fontsize=10)
axs[2, 1].tick_params(axis='x', labelsize=10)
axs[2, 1].tick_params(axis='y', labelsize=8)
axs[2, 1].set_ylabel('s', fontsize=8)
axs[2, 1].bar(x, dsdata, color=colors, yerr=errds)
for i, v in enumerate(dsdata):
    axs[2, 1].text(i - 0.40, dsdata[i], dsdata[i], fontsize=7, color="gray", fontweight='bold')
for i, v in enumerate(dsref):
    axs[2, 1].text(i - 0.38, dsdata_[i], dsref_[i], fontsize=10, color="white", fontweight='bold')

swdata = [0.2, round(Both_Step_Width,2), round(Left_Step_Width,2), round(Right_Step_Width,2)]
swdata_ = [0.2/2, Both_Step_Width/2, Left_Step_Width/2, Right_Step_Width/2]
errsw = [0.05, Both_Step_Width_SD, Left_Step_Width_SD, Right_Step_Width_SD]
swref = [100, SWB, SWL, SWR]
swref_ = [str(100) + "%", str(SWB) + "%", str(SWL) + "%", str(SWR) + "%"]
axs[3, 0].set_title('Step Width', fontsize=10)
axs[3, 0].tick_params(axis='x', labelsize=10)
axs[3, 0].tick_params(axis='y', labelsize=8)
axs[3, 0].set_ylabel('m', fontsize=8)
axs[3, 0].bar(x, swdata, color=colors, yerr=errsw)
for i, v in enumerate(swdata):
    axs[3, 0].text(i - 0.40, swdata[i], swdata[i], fontsize=7, color="gray", fontweight='bold')
for i, v in enumerate(swref):
    axs[3, 0].text(i - 0.38, swdata_[i], swref_[i], fontsize=10, color="white", fontweight='bold')

#spdata = [60.73, 60, 60, 60]
#errsp = [5, 5, 5, 5]
#axs[3, 1].set_title("Stance Phase", fontsize=10)
#axs[3, 1].tick_params(axis='x', labelsize=10)
#axs[3, 1].tick_params(axis='y', labelsize=8)
#axs[3, 1].set_ylabel('% Gait Cycle', fontsize=8)
#axs[3, 1].bar(x, spdata, color=colors, yerr=errsp)

footprogdata = [60.73, 60, 60, 60]
errfp = [5, 5, 5, 5]
#axs[3, 1].set_title("Foot progression", fontsize=10)
#axs[3, 1].tick_params(axis='x', labelsize=10)
#axs[3, 1].tick_params(axis='y', labelsize=8)
#axs[3, 1].set_ylabel('Angle', fontsize=8)
#axs[3, 1].bar(x, footprogdata, color=colors, yerr=errsp)
#line_1 = Line2D([0,2], [0,2], linewidth=1, linestyle = "-", color="blue")
#line_2 = Line2D([0,1], [0,3], linewidth=1, linestyle = "-", color="red")
#axs[3,1].add_line(line_1)
#axs[3,1].add_line(line_2)

plt.plot(3,1, color = 'red', marker = 'o')
r = 1.5
angles = linspace(0 * pi, 2 * pi, 100)
print(angles)
xs = cos(angles)
ys = sin(angles)

plt.plot(xs, ys, color = 'green')
plt.xlim(-r, r)
plt.ylim(-r, r)
plt.gca().set_aspect('equal')

plt.plot(r-0.5, 0, marker = 'P', color = 'blue')
plt.plot(-r+0.5, 0, marker = 'o', color = 'red')
plt.plot([r, -r], [0, 0], color = 'red')

def deg2rad(deg):
    return deg * pi / 180

plt.plot([0, r * cos(deg2rad(90))], [0, r * sin( deg2rad(90))], color = "red")
plt.plot([0, r * cos(deg2rad(45))], [0, r * sin( deg2rad(45))], color = "black")



#fig.suptitle("Temporospatial " + "Test" + " " + "Test2",  y=0.02, fontsize=8, color='gray')
fig.suptitle("TS Graphs Average(SD) " + "AXNB",  y=0.02, fontsize=8, color='gray')

#plt.savefig(self.graph_type + "_Temporospatial_Avg.png")

plt.show()

