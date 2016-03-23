Summary:	ChakraCore is the core part of the Chakra JavaScript engine that powers Microsoft Edge
Name:		ChakraCore
Version:	0.1
Release:	0.1
License:	MIT
Group:		X11/Libraries
# NOTE: not storing on distfiles, until this package is actually useful
Source0:	https://github.com/Microsoft/ChakraCore/archive/linux/ChakraCore.tar.gz
URL:		https://github.com/Microsoft/ChakraCore
BuildRequires:	clang >= 3.5
BuildRequires:	cmake >= 3.2
ExclusiveArch:	%{ix86} %{x8664} arm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# clang does not like these
%define		filterout_c -fvar-tracking-assignments
%define		filterout_cxx -fvar-tracking-assignments

%description
ChakraCore is the core part of Chakra, the high-performance JavaScript
engine that powers Microsoft Edge and Windows applications written in
HTML/CSS/JS. ChakraCore supports Just-in-time (JIT) compilation of
JavaScript for x86/x64/ARM, garbage collection, and a wide range of
the latest JavaScript features. ChakraCore also supports the
JavaScript Runtime (JSRT) APIs, which allows you to easily embed
ChakraCore in your applications.

%prep
%setup -qc
mv ChakraCore-*/* .

%build
install -d build
cd build
CC=$(which clang)
CXX=$(which clang)
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.txt THIRD-PARTY-NOTICES.txt CONTRIBUTING.md CODE_OF_CONDUCT.md
