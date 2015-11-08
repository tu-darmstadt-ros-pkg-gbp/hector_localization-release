Name:           ros-jade-hector-pose-estimation-core
Version:        0.2.1
Release:        0%{?dist}
Summary:        ROS hector_pose_estimation_core package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/hector_pose_estimation_core
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-jade-geographic-msgs
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-nav-msgs
Requires:       ros-jade-rosconsole
Requires:       ros-jade-roscpp
Requires:       ros-jade-rostime
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-tf
BuildRequires:  eigen3-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-geographic-msgs
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-nav-msgs
BuildRequires:  ros-jade-rosconsole
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rostime
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-tf

%description
hector_pose_estimation_core is the core package of the hector_localization
stack. It contains the Extended Kalman Filter (EKF) that estimates the 6DOF pose
of the robot. hector_pose_estimation can be used either as a library, as a
nodelet or as a standalone node.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sun Nov 08 2015 Johannes Meyer <meyer@fsr.tu-darmstadt.de> - 0.2.1-0
- Autogenerated by Bloom

