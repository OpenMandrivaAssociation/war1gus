Name:		war1gus
Summary:	Warcraft: Orc & Humans data game set for the Stratagus engine (need game data)
Version:	3.0.0
Release:	1
Source0:	https://github.com/Wargus/war1gus/archive/v%{version}/%{name}-%{version}.tar.gz
URL:		https://stratagus.com/war1gus.html
Group:		Games/Strategy
License:	GPLv2
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:  ImageMagick
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
BuildRequires:	stratagus-devel = %{version}

Requires:	cdparanoia
Requires:	stratagus = %{version}
Recommends:	ffmpeg
Recommends:	ffmpeg2theora

%description
War1gus is a re-implementation of “Warcraft: Orcs & Humans” that allows you to play Warcraft with the Stratagus engine.
The game uses graphics and sounds from the original Warcraft, 
but improves the gameplay mechanisms with many modern conveniences that the Stratagus engine allows, 
such as modern mouse controls, named groups, larger group selection, more player factions in multiplayer games, a map editor, and multiple towns. 
  
During the first start of War1gus you will be asked for a copy of the original Warcraft, so that the installer can extract the data. 
Both the DOS CD and Floppy versions should work. Extracting the data from demo, shareware.

%prep
%autosetup -p1

%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%doc README.md doc/*
%{_gamesbindir}/%{name}
%{_bindir}/war1gus
%{_bindir}/war1tool
%{_gamesdatadir}/stratagus/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop



%changelog
* Thu Sep 27 2012 Zombie Ryushu <ryushu@mandriva.org> 2.2.7-1mdv2012.0
+ Revision: 817687
- remove old patches
- Upgrade to 2.2.7

* Mon Jan 30 2012 Andrey Bondrov <abondrov@mandriva.org> 2.2.6-1
+ Revision: 769857
- Add patch0 and patch1 to fix build in Cooker (DSO and png issues)
- imported package wargus
