# -*- coding: utf-8 -*-
"""
.. module:: main_convert_APS_1ID.py
   :platform: Unix
   :synopsis: Convert APS 1-ID TIFF files in data exchange.

.. moduleauthor:: Francesco De Carlo <decarlof@gmail.com>


""" 
from dataio.data_exchange import DataExchangeFile, DataExchangeEntry
from dataio.data_convert import Convert

import re

#def main():

file_name = '/local/data/databank/APS_1_ID/APS1ID_Cat4B_2/CAT4B_2_.tif'
log_file = '/local/data/databank/APS_1_ID/APS1ID_Cat4B_2/CAT4B_2_TomoStillScan.dat'

hdf5_file_name = '/local/data/databank/dataExchange/microCT/CAT4B_2.h5'

verbose = True

if verbose: print file_name
if verbose: print log_file
if verbose: print hdf5_file_name



#Read input APS 1-ID log file data
file = open(log_file, 'r')
if verbose: print '###############################'
##for line in file:
##    if verbose: print line
##
##    if 'Number of darks' in line:
##        NumberOfDarks = re.findall(r'\d+', line)
##        if verbose: print 'Number of Darks', NumberOfDarks[0]
##    if 'Number of flats' in line:
##        NumberOfFlats = re.findall(r'\d+', line)
##        if verbose: print 'Number of Flats', NumberOfFlats[0]
##    if 'Number of projections' in line:
##        NumberOfProjections = re.findall(r'\d+', line)
##        if verbose: print 'Number of Projections', NumberOfProjections[0]
##    if 'Number of inter-flats' in line:
##        NumberOfInterFlats = re.findall(r'\d+', line)
##        if verbose: print 'Number of inter-flats', NumberOfInterFlats[0]
##    if 'Inner scan flag' in line:
##        InnerScanFlag = re.findall(r'\d+', line)
##        if verbose: print 'Inner scan flag', InnerScanFlag[0]
##    if 'Flat frequency' in line:
##        FlatFrequency = re.findall(r'\d+', line)
##        if verbose: print 'Flat frequency', FlatFrequency[0]
##    if 'Rot Y min' in line:
##        RotYmin = re.findall(r'\d+.\d+', line)
##        if verbose: print 'Rot Y min', RotYmin[0]
##    if 'Rot Y max' in line:
##        RotYmax = re.findall(r'\d+.\d+', line)
##        if verbose: print 'Rot Y max', RotYmax[0]
##    if 'Angular step' in line:
##        AngularStep = re.findall(r'\d+.\d+', line)
##        if verbose: print 'Angular step', AngularStep[0]
##if verbose: print '###############################'
file.close()

##dark_start = 1
##dark_end = int(NumberOfDarks[0]) + 1
##white_start = dark_end
##white_end = white_start + int(NumberOfFlats[0])
##projection_start = white_end
##projection_end = projection_start + int(NumberOfProjections[0])


projections_start = 943
projections_end = 1853
white_start = 1844
white_end = 1853
dark_start = 1854
dark_end = 1863

if verbose: print dark_start, dark_end
if verbose: print white_start, white_end
if verbose: print projections_start, projections_end

### if testing uncomment
##projections_end = 952
##white_end = 1846
##dark_end = 1856


mydata = Convert()
# Create minimal hdf5 file
mydata.series_of_images(file_name,
                 hdf5_file_name,
                 projections_start,
                 projections_end,
                 white_start = white_start,
                 white_end = white_end,
                 dark_start = dark_start,
                 dark_end = dark_end,
                 digits = 6,
                 verbose = False
                 )

 
# Add extra metadata if available

# Open DataExchange file
f = DataExchangeFile(hdf5_file_name, mode='a') 

# Create HDF5 subgroup
# /measurement/instrument
f.add_entry( DataExchangeEntry.instrument(name={'value': 'APS 1-ID Tomography'}) )

# Create HDF5 subgroup
# /measurement/instrument/source
f.add_entry( DataExchangeEntry.source(name={'value': 'Advanced Photon Source'},
                                    date_time={'value': "2012-07-08T15:42:56+0100"},
                                    beamline={'value': "1-ID"},
                                    current={'value': 100.96, 'units': 'mA', 'dataset_opts': {'dtype': 'd'}},
                                    )
)

# Create HDF5 subgroup
# /measurement/instrument/monochromator
f.add_entry( DataExchangeEntry.monochromator(type={'value': 'unknow'},
                                            energy={'value': 65, 'units': 'keV', 'dataset_opts': {'dtype': 'd'}},
                                            mono_stripe={'value': 'unknow'},
                                            )
    )

# Create HDF5 subgroup
# /measurement/experimenter
f.add_entry( DataExchangeEntry.experimenter(name={'value':"Peter Kenesei"},
                                            role={'value':"Project PI"},
                                            affiliation={'value':"Advanced Photon Source"},
                                            phone={'value':"+1 630 252-0133"},
                                            email={'value':"kenesei@aps.anl.gov"},

                )
    )


f.close()
if verbose: print "Done converting ", file_name

###if __name__ == "__main__":
###    main()

