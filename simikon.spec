Summary:	Microcontrollers MCS51 simulator
Summary(pl):	Symulator mikrokontrolerów MCS51
Name:		simikon
Version:	0.0.8
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Applications
Source0:	http://simikon.sourceforge.net/%{name}-%{version}.tar.bz2
Patch0:		%{name}-make.patch
URL:		http://simikon.sourceforge.net/
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
SiMiKON intends to be a full featured simulator for simulating MCS51
family of microcontrollers. It's written in C++ using QT widget set.
It consists of code editor, IHEX disassembler, and several modules:
registers, sfr, stack, memory, I/O ports, serial, interrupts and
performance analyzer. It's in early stages of development and buggy as
hell, but it's already a bit useful. Many of this modules lack some
functionality and need to be rewritten.

%description -l pl
SiMiKON w zamierzeniu ma byæ pe³nym symulatorem mikrokontrolerów
rodziny MCS51. Zawiera on edytor kodu, disassembler IHEX oraz kilka
modu³ów: rejestry, sfr, stos, pamiêæ, porty I/O, porty szeregowe,
przerwania oraz analizator wydajno¶ci.

%prep
%setup -q
%patch0 -p1

%build
QTDIR=%{_prefix}; export QTDIR
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO doc/*.{html,gif,jpg}
%attr(755,root,root) %{_bindir}/*
