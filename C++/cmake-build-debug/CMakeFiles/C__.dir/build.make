# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.8

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /cygdrive/c/Users/100514971/.CLion2017.2/system/cygwin_cmake/bin/cmake.exe

# The command to remove a file.
RM = /cygdrive/c/Users/100514971/.CLion2017.2/system/cygwin_cmake/bin/cmake.exe -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++/cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/C__.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/C__.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/C__.dir/flags.make

CMakeFiles/C__.dir/main.cpp.o: CMakeFiles/C__.dir/flags.make
CMakeFiles/C__.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/C__.dir/main.cpp.o"
	/usr/bin/c++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/C__.dir/main.cpp.o -c "/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++/main.cpp"

CMakeFiles/C__.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/C__.dir/main.cpp.i"
	/usr/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++/main.cpp" > CMakeFiles/C__.dir/main.cpp.i

CMakeFiles/C__.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/C__.dir/main.cpp.s"
	/usr/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++/main.cpp" -o CMakeFiles/C__.dir/main.cpp.s

CMakeFiles/C__.dir/main.cpp.o.requires:

.PHONY : CMakeFiles/C__.dir/main.cpp.o.requires

CMakeFiles/C__.dir/main.cpp.o.provides: CMakeFiles/C__.dir/main.cpp.o.requires
	$(MAKE) -f CMakeFiles/C__.dir/build.make CMakeFiles/C__.dir/main.cpp.o.provides.build
.PHONY : CMakeFiles/C__.dir/main.cpp.o.provides

CMakeFiles/C__.dir/main.cpp.o.provides.build: CMakeFiles/C__.dir/main.cpp.o


CMakeFiles/C__.dir/Sensoduino.cpp.o: CMakeFiles/C__.dir/flags.make
CMakeFiles/C__.dir/Sensoduino.cpp.o: ../Sensoduino.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/C__.dir/Sensoduino.cpp.o"
	/usr/bin/c++.exe  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/C__.dir/Sensoduino.cpp.o -c "/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++/Sensoduino.cpp"

CMakeFiles/C__.dir/Sensoduino.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/C__.dir/Sensoduino.cpp.i"
	/usr/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++/Sensoduino.cpp" > CMakeFiles/C__.dir/Sensoduino.cpp.i

CMakeFiles/C__.dir/Sensoduino.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/C__.dir/Sensoduino.cpp.s"
	/usr/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++/Sensoduino.cpp" -o CMakeFiles/C__.dir/Sensoduino.cpp.s

CMakeFiles/C__.dir/Sensoduino.cpp.o.requires:

.PHONY : CMakeFiles/C__.dir/Sensoduino.cpp.o.requires

CMakeFiles/C__.dir/Sensoduino.cpp.o.provides: CMakeFiles/C__.dir/Sensoduino.cpp.o.requires
	$(MAKE) -f CMakeFiles/C__.dir/build.make CMakeFiles/C__.dir/Sensoduino.cpp.o.provides.build
.PHONY : CMakeFiles/C__.dir/Sensoduino.cpp.o.provides

CMakeFiles/C__.dir/Sensoduino.cpp.o.provides.build: CMakeFiles/C__.dir/Sensoduino.cpp.o


# Object files for target C__
C___OBJECTS = \
"CMakeFiles/C__.dir/main.cpp.o" \
"CMakeFiles/C__.dir/Sensoduino.cpp.o"

# External object files for target C__
C___EXTERNAL_OBJECTS =

C__.exe: CMakeFiles/C__.dir/main.cpp.o
C__.exe: CMakeFiles/C__.dir/Sensoduino.cpp.o
C__.exe: CMakeFiles/C__.dir/build.make
C__.exe: CMakeFiles/C__.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable C__.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/C__.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/C__.dir/build: C__.exe

.PHONY : CMakeFiles/C__.dir/build

CMakeFiles/C__.dir/requires: CMakeFiles/C__.dir/main.cpp.o.requires
CMakeFiles/C__.dir/requires: CMakeFiles/C__.dir/Sensoduino.cpp.o.requires

.PHONY : CMakeFiles/C__.dir/requires

CMakeFiles/C__.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/C__.dir/cmake_clean.cmake
.PHONY : CMakeFiles/C__.dir/clean

CMakeFiles/C__.dir/depend:
	cd "/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++" "/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++" "/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++/cmake-build-debug" "/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++/cmake-build-debug" "/cygdrive/c/Users/100514971/Google Drive/Learn to Program/Github/ScratchPad/C++/cmake-build-debug/CMakeFiles/C__.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/C__.dir/depend

