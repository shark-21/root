from ROOT import TH1F,TCanvas
import numpy as np

# Generate data (efficiently using vectorized operations)
num_data = 10000    
data = np.random.normal(loc=10, scale=3, size=num_data)
weights = np.random.rand(num_data)  

# Create ROOT histogram (using efficient TH1D constructor)
hist = TH1F("my_hist", "Normally Distributed Data", 50, 4, 16)  # 50 bins from 4 to 16
for i in range(num_data):
    hist.Fill(data[i], weights[i])
# Fill the histogram (efficient vectorized filling)
c1=TCanvas()
# Optional: Draw the histogram (using efficient TH1D::Draw)
hist.Draw()
# ROOT.gApplication.Run()
input()