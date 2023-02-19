import os
import sys

class deploy_vhdl_project_class:

    def __init__(self, project_name):

        self.project_name = project_name


        self.makefile_header = """# ========================================== #
#
# Makefile for {0} Project
#
# Author  : J.P
# Version : 1.0 
# 
# ========================================== #
""".format(self.project_name)


        self.makefile_configuration = """
# == Makefile Configuration ==
SEL_STATION=LINUX
ROOT=$(PWD)/..
PROJECT_NAME={0}
WORK_DIR={1}_WORK
TRANSCRIPT_EN=OFF
# ============================
""".format(self.project_name, self.project_name.upper())


        self.makefile_src_dir = """
# == SOURCES DIRECTORY ==
SRC_{0}_DIR=~/Documents/GitHub/VHDL_code/TBD_a_completer
# =======================
""".format(self.project_name.upper())
    

        self.makefile_design_lib = """
# == DESIGN LIBRARIES ==
# -- ADD Here your design libraries
# ======================
"""

        self.makefile_tb_lib = """
# == TESTBENCH LIBRARIES ==
# -- ADD Here your testbench library
# =========================
"""

        self.makefile_lib_list = """
# ==  LIB LIST ==
LIB_LIST+=
# ================
"""

        self.makefile_all = """
all: print_generic_rules
	@echo ""
	@echo "Makefile for {0} blocks tests"
	@echo ""
	@echo "== SOURCES COMPILATIONS =="
	@echo ""
	@echo "- Design Sources Compilation :"
	@echo "make compile_design"
	@echo ""	
	@echo "- Compile Testbench :"
	@echo "make compile_testbench"
	@echo ""
	@echo "- Compile Design & Testbench :"
	@echo "make compile_all"
	@echo ""
	@echo "=========================="
	@echo ""
	@echo "== RUN TESTS =="
	@echo "- Run Test of XXXXX"
	@echo "make run_tb_XXXXX TEST=[TEST_NB]"
	@echo "==============="
	@echo ""
	@echo "== SCENARII LIST =="
	@echo "$(SCN_LIST)"
	@echo "==================="
""".format(self.project_name.upper())


    
        self.design_vhdl_list = """
# == DESIGN VHD FILE LIST ==
# -- Add Here your design list
# ==========================
"""

        self.tb_custom_v_list = """
# == TESTBENCH {0}  VERILOG Custom FILES LIST ==
# -- Add Here your Specific verilog custom testbench file
# =================================
"""

        self.tb_generic_v_list = """
# == Specific Testbench File List ==
# -- Complete Here the name of the library
src_tb_lib_XXXXX_v+=$(TB_SRC_DIR)/tb_lib_XXXXX/testbench_setup.sv
src_tb_lib_XXXXX_v+=$(TB_SRC_DIR)/tb_lib_XXXXX/clk_gen.sv
src_tb_lib_XXXXX_v+=$(TB_SRC_DIR)/tb_lib_XXXXX/tb_top.sv
# ==================================
"""

        self.compile_design_targets = """
## == COMPILE DESIGN == ##

# -- Add here targets for design compilation

# Compile Lib XXXXX
compile_XXXXX:
	make compile_design_vhd_files SRC_VHD="$(src_vhd_lib_XXXXX)" VHD_DESIGN_LIB=$(LIB_XXXXX)

# ====================== #
"""

        self.compile_tb_targets = """
## == COMPILE TESTBENCH == ##

# -- Add Here targets for testbenchs compilation
compile_testbench_sources:
	make compile_tb_v_files SRC_TB_V="$(src_tb_v)" TB_LIB_TOP=$(LIB_TB_XXXXX)
	make compile_tb_v_files SRC_TB_V="$(src_tb_lib_XXXXX_v)" TB_LIB_TOP=$(LIB_TB_XXXXX)
# ========================= #
"""

        self.scn_list = """
# == SCENARII LIST ==

# -- Add here the list of scenarii
SCN_LIST +=

# ===================
"""


        self.lib_args = """
# == LIB ARGS ==
# -- Complete here the library use for running a test with vsim
LIB_ARGS=-L lib_XXXX -L lib_YYYY
# ==============
"""

        self.run_test_targets = """
# == RUN TEST ==
# -- Add here targets for running tests
run_tb_XXXXX:
	make run_test TRANSCRIPT_EN=ON DO_FILES_EN=ON
# ==============
"""

        self.makefile_includes = """
# == MAKEFILE Includes ==
include ~/Documents/GitHub/VHDL_code/Makefile/MakefileGeneric
include ~/Documents/GitHub/VHDL_code/Makefile/MakefileGHDL
include ~/Documents/GitHub/VHDL_code/Makefile/MakefileSonarqube
# =======================
"""



    

        # Makefile Template string to create
        self.makefile_template = "\n".join(
            [self.makefile_header,
             self.makefile_configuration,
             self.makefile_src_dir,
             self.makefile_design_lib,
             self.makefile_tb_lib,
             self.makefile_lib_list,
             self.makefile_all,
             self.design_vhdl_list,
             self.tb_custom_v_list,
             self.tb_generic_v_list,
             self.compile_design_targets,
             self.compile_tb_targets,
             self.scn_list,
             self.lib_args,
             self.run_test_targets,
             self.makefile_includes]
        )

