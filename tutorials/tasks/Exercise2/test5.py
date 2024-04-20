from ROOT import *


def project_histogram_1d(h2, xfirst, xlast, yfirst, ylast):
  
 # Get dimensions of the histogram
  n_dims = h2.GetDimension()
  n_bins_x = h2.GetXaxis().GetNbins()

  # Check for valid x-axis range
  if xfirst < 1 or xfirst > n_bins_x or xlast < xfirst or xlast > n_bins_x:
    print("Error: Invalid x-axis range. Please provide values within the original histogram's range (1 to", n_bins_x, ").")
    return None


  
  # Create the projected 1D histogram
  hist_proj = TH1F("hist_proj", "Projection of " + h2.GetTitle(), xlast - xfirst + 1,
                     h2.GetXaxis().GetBinLowEdge(xfirst), h2.GetXaxis().GetBinUpEdge(xlast))

  # Loop through bins in the x-axis range and sum counts over the y-axis range
  for i in range(xfirst, xlast + 1):
    # Initialize the projected bin content
    hist_proj.SetBinContent(i - xfirst + 1, 0)
    for j in range(yfirst, ylast + 1):
      # Sum the content of the corresponding bin in the multidimensional histogram
      hist_proj.SetBinContent(i - xfirst + 1, hist_proj.GetBinContent(i - xfirst + 1) + h2.GetBinContent(i, j))

  return hist_proj

# Create a 2D histogram. Following h2:  X axis has 12bins ranging 0 to 10; Y axix has 6bins from 0 to 5.
h2 = TH2F("h2_example", "Example 2D Histogram", 12, 0, 10, 6, 0, 5)
for i in range(1, h2.GetNbinsX() + 1):
  for j in range(1, h2.GetNbinsY() + 1):
    value = i * j
    h2.SetBinContent(i, j, value)

projected_hist= project_histogram_1d(h2, 2,5,1,2 )
c1=TCanvas()

projected_hist.Draw()
c2 = TCanvas()
h2.Draw()
input()

 