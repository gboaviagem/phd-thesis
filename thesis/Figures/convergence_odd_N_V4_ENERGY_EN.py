import matplotlib.pyplot as plt
import numpy as np
np.seterr(divide='ignore', invalid='ignore')
# Locale settings (to use comma instead of point as decimal separator)
# import locale
# locale.setlocale(locale.LC_NUMERIC, "de_DE")
# Tell matplotlib to use the locale we set above
# plt.rcParams['axes.formatter.use_locale'] = True
from matplotlib import rc
# rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)
# ---------------------------------------------------------

fig = plt.figure()
ax1 = fig.add_subplot(111)


N_list = np.round(np.logspace(1, 3, num=10, endpoint=True, base=10.0))
for i in range(len(N_list)):
	N_list[i] = N_list[i] + (N_list[i]%2) + 1 # makes all entries of N_list odd

a_list = np.array([0.0,0.2,0.4,0.5,0.7,0.9,1.0])

colors = ['#FA3900', '#FABD00', '#BADF00',
		  '#00DF70', '#00B0DF', '#0070DF',
		  '#4700C4', '#AA00FF', '#FF00D8']

for i in range(len(a_list)):
	a = a_list[i]
	color = colors[i]
	errors = [] # array of element-wise error
	for N in N_list:
		n = np.arange(-(N-1)/2,(N-1)/2 + 1)
		
# 		h_lpf_odd = np.zeros(N)
# 		for i in range(N):
# 			if n[i] != 0:
# 				h_lpf_odd[i] = (1./N) * np.sin(np.pi*(n[i]-a))/np.sin(np.pi*(n[i]-a)/N)
# 			else:
# 				h_lpf_odd[i] = 1.0
		
		h_lpf_odd = (1/N) * np.sin(np.pi*(n-a))/np.sin(np.pi*(n-a)/N)
		# at integer values of "a", np.sin(np.pi*(n-a)/N) will be zero for some value of "n". The following two lines will handle it, setting the value of h_lpf_odd to 1, which is its actual limit.
		check_nan = np.isnan(h_lpf_odd)
		h_lpf_odd[np.where(check_nan == True)] = 1.0
		
		sinc = np.sinc(n-a)
		total_sinc_energy = np.sum(np.abs(sinc)**2)
	
		average_error_percentage = 100* np.sum(np.abs(h_lpf_odd-sinc)**2)/total_sinc_energy
		errors.append(average_error_percentage)
	
	m = 'o'
	if a==0:
		m = '+'
	if a==1:
		m = 'x'
	
# 	str_frac_parameter = str(a).replace('.',',')
	str_frac_parameter = str(a).replace('.','.')
	
	ax1.scatter(N_list,errors,s=70,c=color,marker=m,label=r'$a$ = ' + str_frac_parameter)
	
# PLOTTING -------------------

plotpath = 'convergence_odd_N_V4_ENERGY_EN.pdf'
font = 20
plt.legend(fontsize=font-2)

plt.plot(N_list,np.zeros(len(N_list)),'k--') # Black line at y = 0.
plt.xscale('log')
# plt.ylim([-0.2,7])
plt.xlim([0.8*np.min(N_list),np.max(N_list)])
plt.title(r'$E\{\mathbf{h}_a - \mathbf{h}_{LPF}\}/E\{\mathbf{h}_{LPF}\}$ \ \ \ (odd $N$)',fontsize=font)
plt.xlabel(r'Filter length',fontsize=font)
plt.ylabel(r'Relative error (\%)',fontsize=font)
plt.axis('tight')
plt.tick_params(axis='both', which='major', labelsize=font-2)
plt.savefig(plotpath, bbox_inches="tight",format='pdf')


plt.show()
