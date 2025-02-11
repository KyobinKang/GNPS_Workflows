#!/usr/bin/python


import sys
import getopt
import os
import json
import argparse
import ming_proteosafe_library
import ming_fileio_library

def main():
    parser = argparse.ArgumentParser(description='Create parallel parameters')
    parser.add_argument('workflow_parameters', help='proteosafe xml parameters')
    parser.add_argument('input_mgf', help='Input mgf file to network')
    parser.add_argument('library_folder', help='library_folder')
    parser.add_argument('library_matches', help='output matches')
    parser.add_argument('binary_path', help='binary_path')
    args = parser.parse_args()

    params_object = ming_proteosafe_library.parse_xml_file(open(args.workflow_parameters))

    library_files = ming_fileio_library.list_files_in_dir(args.library_folder)

    temp_parameters_file = "temp_parameters" + ".params"

    output_parameter_file = open(temp_parameters_file, "w")
    #Search Criteria

    output_parameter_file.write("SCORE_THRESHOLD=%s\n" % (params_object["SCORE_THRESHOLD"][0]))
    output_parameter_file.write("MIN_MATCHED_PEAKS_SEARCH=%s\n" % (params_object["MIN_MATCHED_PEAKS"][0]))
    output_parameter_file.write("TOP_K_RESULTS=%s\n" % (params_object["TOP_K_RESULTS"][0]))
    output_parameter_file.write("search_peak_tolerance=%s\n" % (params_object["tolerance.Ion_tolerance"][0]))
    output_parameter_file.write("search_parentmass_tolerance=%s\n" % (params_object["tolerance.PM_tolerance"][0]))
    output_parameter_file.write("ANALOG_SEARCH=%s\n" % (params_object["ANALOG_SEARCH"][0]))
    output_parameter_file.write("MAX_SHIFT_MASS=%s\n" % (params_object["MAX_SHIFT_MASS"][0]))

    #Filtering Criteria
    output_parameter_file.write("FILTER_PRECURSOR_WINDOW=%s\n" % (params_object["FILTER_PRECURSOR_WINDOW"][0]))
    output_parameter_file.write("MIN_PEAK_INT=%s\n" % (params_object["MIN_PEAK_INT"][0]))
    output_parameter_file.write("WINDOW_FILTER=%s\n" % (params_object["WINDOW_FILTER"][0]))
    output_parameter_file.write("FILTER_LIBRARY=%s\n" % (params_object["FILTER_LIBRARY"][0]))

    output_parameter_file.write("EXISTING_LIBRARY_MGF=%s\n" % (" ".join(library_files)))

    output_parameter_file.write("RESULTS_DIR=%s\n" % (args.library_matches))
    output_parameter_file.write("searchspectra=%s\n" % (args.input_mgf))


    output_parameter_file.close()

    cmd = "%s ExecSpectralLibrarySearchMolecular %s -ll 0" % (args.binary_path, temp_parameters_file)
    os.system(cmd)

if __name__ == "__main__":
    main()
