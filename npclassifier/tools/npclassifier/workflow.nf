#!/usr/bin/env nextflow

params.inputfile = ''
params.workflowParameters = ''

_file_ch = Channel.fromPath( params.inputfile )

TOOL_FOLDER = "$baseDir/bin"
params.publishdir = "nf_output"

process calculateResults {
    publishDir "$params.publishdir", mode: 'copy'

    input:
    file input_file from _file_ch.first()

    output:
    file "result_file.tsv"

    """
    python $TOOL_FOLDER/npclassify.py \
        "$input_file" \
        "result_file.tsv"
    """
}
