#
# TODO:
# - review BRs
#
# Conditional build:
#
%define		kfname	kuserfeedback
Summary:	Kuser feedback
Name:		kuserfeedback
Version:	1.2.0
Release:	1
License:	BSD-3-Clause, MIT
Group:		X11/Applications
Source0:	https://download.kde.org/stable/kuserfeedback/%{name}-%{version}.tar.xz
# Source0-md5:	905f3e9686c15814594956bea084da64
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	bison
BuildRequires:	cmake
BuildRequires:	flex
BuildRequires:	kf5-extra-cmake-modules >= 5.26
BuildRequires:	qt5-build
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Framework for collecting feedback from application users via telemetry
and targeted surveys.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}


%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md
%{_datadir}/qlogging-categories5/org_kde_UserFeedback.categories
%{_libdir}/libKUserFeedbackCore.so.1.*.*
%ghost %{_libdir}/libKUserFeedbackCore.so.1
%{_libdir}/libKUserFeedbackWidgets.so.1.*.*
%ghost %{_libdir}/libKUserFeedbackWidgets.so.1
%dir %{_libdir}/qml/org/kde/userfeedback
%{_libdir}/qml/org/kde/userfeedback/libKUserFeedbackQml.so
%{_libdir}/qml/org/kde/userfeedback/qmldir

%files devel
%defattr(644,root,root,755)
%{_libdir}/cmake/KUserFeedback
%{_libdir}/libKUserFeedbackCore.so
%{_libdir}/libKUserFeedbackWidgets.so
%{_includedir}/KUserFeedback
%{_prefix}/mkspecs/modules/qt_KUserFeedbackCore.pri
%{_prefix}/mkspecs/modules/qt_KUserFeedbackWidgets.pri
