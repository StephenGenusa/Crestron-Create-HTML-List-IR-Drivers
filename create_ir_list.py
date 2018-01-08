import os

"""
Copyright 2018 by Stephen Genusa

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""


rec_seps = map(chr, range(1, 32))
rec_seps += map(chr, range(128, 256))
BUFFER_LEN = 200

def get_ir_info(filename):
    field_pos = 1
    field_val = ""
    f = open(filename, "rb")
    buffer = f.read(BUFFER_LEN)
    f.close()
    rec_values = []
    rec_values.append(filename)
    for i in range(0, BUFFER_LEN):
        if buffer[i] in rec_seps:
            if field_pos > 18:
                break
            rec_values.append(field_val)
            field_pos += 1
            field_val = ""
        else:
            field_val += buffer[i]
    if len(rec_values) < 19:
        rec_values.extend([''] * 10)
    return rec_values


rec_values_count = []    
rec_values_count.extend([0] * 19)
htmlfilename = "crestron_ir_list.html"
ir_files = []
ir_files += [each for each in os.listdir(".") if each.endswith(".ir")]
with open(htmlfilename, "w") as htmlfile:
    htmlfile.write("<html><body><table border=\"3\"><tr><th colspan=\"17\"><h3><br>Crestron IR Drivers</h3></th></tr>")    
    for ir_file in ir_files:
        ir_info = get_ir_info(ir_file)
      
        htmlfile.write("<tr>")
        for index, info in enumerate(ir_info):
            if index not in [1, 2] and index < 19:
                htmlfile.write("<td>" + info + "</td>")
        htmlfile.write("</tr>")
    htmlfile.write("</table></body></html>")
print htmlfilename, "created"