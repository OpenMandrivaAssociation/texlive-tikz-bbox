Name:		texlive-tikz-bbox
Version:	57444
Release:	2
Summary:	Precise determination of bounding boxes in TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-bbox
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-bbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-bbox.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The built-in determination of the bounding box in TikZ is not
entirely accurate. This is because, for Bezier curves, it is
the smallest box that contains all control points, which is in
general larger than the box that just contains the curve. This
library determines the exact bounding box of the curve.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikz-bbox
%doc %{_texmfdistdir}/doc/latex/tikz-bbox

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
