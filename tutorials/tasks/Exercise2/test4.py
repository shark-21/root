from ROOT import *
import numpy as np



def reduce_rebin_Hist(h, ifirst, ilast, rebin_factor):
    # Clone the original histogram
    h_clone = h.Clone("h_clone")

    # Rebin the cloned histogram
    h_clone.Rebin(rebin_factor)
    reduced_histogram = TH1F("reduced_histogram", "Reduced-Rebinned Histogram", ilast - ifirst + 1, ifirst, ilast + 1)
    print(h_clone.GetNbinsX())
    # Filling the new histogram with the summed bin contents from the original histogram
    for i in range(ifirst, ilast + 1):
        reduced_histogram.SetBinContent(i - ifirst + 1, h_clone.GetBinContent(i))
    return reduced_histogram
    
num_data = 10000    
data = np.random.normal(loc=10, scale=3, size=num_data)
weights = np.random.rand(num_data)  

# Create ROOT histogram (using efficient TH1D constructor)
hist = TH1F("my_hist", "Normally Distributed Data", 50, 4, 16)  # 50 bins from 4 to 16
for i in range(num_data):
    hist.Fill(data[i], weights[i])
h_reduced =reduce_rebin_Hist(hist,9,18,2)
c1=TCanvas()
h_reduced.Draw()
input()
