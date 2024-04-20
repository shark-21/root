from ROOT import *
import numpy as np

def reduce_his(h, ifirst, ilast):
  

  # Check for valid range
  print(h.GetNbinsX()) #Range should have less bins than total bins. 
 

  # Create the new histogram with the reduced range
  h_reduced = h.Clone(h.GetName() + "_reduced")
  h_reduced.SetBinContent(h_reduced.GetNbinsX(), h.GetBinContent(ifirst, ilast))
  h_reduced.SetBinError(h_reduced.GetNbinsX(), h.GetBinError(ifirst, ilast))

  # Set axis ranges and labels for the reduced histogram
  h_reduced.GetXaxis().SetRange(ifirst, ilast)
  h_reduced.GetXaxis().SetTitle(h.GetXaxis().GetTitle())
  h_reduced.SetTitle(h.GetTitle() + " (Reduced)")
 
  return h_reduced


num_data = 10000    
data = np.random.normal(loc=10, scale=3, size=num_data)
weights = np.random.rand(num_data)  

# Create ROOT histogram (using efficient TH1D constructor)
hist = TH1F("my_hist", "Normally Distributed Data", 50, 4, 16)  # 50 bins from 4 to 16
for i in range(num_data):
    hist.Fill(data[i], weights[i])
h_reduced =reduce_his(hist,3,7)
c1=TCanvas()
h_reduced.Draw()
input()
