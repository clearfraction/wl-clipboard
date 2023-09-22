Name     : wl-clipboard
Version  : 2.2.1
Release  : 1
URL      : https://github.com/bugaevc/wl-clipboard
Source0  : https://github.com/bugaevc/wl-clipboard/archive/refs/tags/v%{version}.tar.gz
Summary  : Command-line copy/paste utilities for Wayland
Group    : Development/Tools
License  : GPLv3+
BuildRequires : cmake
BuildRequires : buildreq-meson
BuildRequires : wayland-dev wayland-protocols-dev

%description	
Command-line Wayland clipboard utilities, `wl-copy` and `wl-paste`,
that let you easily copy data between the clipboard and Unix pipes,
sockets, files and so on.

%prep
%setup -q -n wl-clipboard-%{version}

%build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
meson \
    --libdir=lib64 --prefix=/usr \
    --buildtype=plain builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
rm -rf %{buildroot}/usr/share/man

%files
%defattr(-,root,root,-)
/usr/bin/wl-copy
/usr/bin/wl-paste
/usr/share/bash-completion/completions/wl-*
/usr/share/zsh/site-functions/_wl-*
/usr/share/fish/vendor_completions.d/wl-copy.fish
/usr/share/fish/vendor_completions.d/wl-paste.fish
