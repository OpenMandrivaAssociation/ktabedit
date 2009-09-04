%define svn_rev 749809
%define libname %mklibname %name 0

Name:           ktabedit 
Version:        0.0.8
Release:        %mkrel 4
Summary:        Powerful Tablature Editor for KDE
License:        GPL
Group:          Sound
URL:            http://ktabedit.sourceforge.net/
# svn co svn://anonsvn.kde.org/home/kde/trunk/playground/multimedia/ktabedit/
Source0:        http://downloads.sourceforge.net/sourceforge/ktabedit/ktabedit-%{svn_rev}.tar.bz2
BuildRequires:  chrpath
BuildRequires:  kdelibs4-devel
BuildRequires:  tse3-devel 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
KTabEdit is basically a guitar tabulature editor for K Desktop Environment.
It's much more than just a tab editor. It's features are:

        * Free GPLed program;
        * K Desktop Environment GUI;
        * Powerful and convenient tabulature editing, including many effects
          and classical note score editing for classic instrument players;
        * Full and very customizable MIDI to tabulature import and export;
        * Support of extra data formats, such as ASCII tabulatures or popular
          programs' format, such as Guitar Pro's or TablEdit;
        * Chord fingering construction tools - chord finder & chord analyzer;
        * Highly customizable to suit a lot of possible instruments (not only
          6-stringed guitars, and even not only guitars), including drum
          tracks, lyrics and other MIDI events.

%prep
%setup -q -n %{name}
%{__perl} -pi -e 's/\r$//g' credit.txt

%build
%{cmake}
%{make}

%install
%{__rm} -rf %{buildroot}
(cd build && %{makeinstall_std} CMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix})
%{_bindir}/chrpath -d %{buildroot}%{_bindir}/ktabedit

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO VERSION credit.txt ktabedit.lsm ktabedit.spec
%defattr(-,root,root,0755)
%attr(0755,root,root) %{_bindir}/ktabedit
%{_datadir}/apps/%{name}
%{_datadir}/apps/ktabedit_part.rc
%{_datadir}/kde4/services/ktabedit_part.desktop
%{_datadir}/mimelnk/application/x-ktabedit.desktop
