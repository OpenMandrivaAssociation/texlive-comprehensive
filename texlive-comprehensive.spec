# revision 16006
# category Package
# catalog-ctan /info/symbols/comprehensive
# catalog-date 2009-11-18 09:39:01 +0100
# catalog-license lppl
# catalog-version 11.0
Name:		texlive-comprehensive
Version:	11.0
Release:	2
Summary:	Symbols accessible from LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/symbols/comprehensive
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comprehensive.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comprehensive.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
Around 5000 symbols are listed as a set of tables. The tables
of symbols are ordered in a logical way (the document begins
with a 'frequently requested symbols' list), the aim being to
make the document a convenient way of looking up symbols.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/comprehensive/README
%doc %{_texmfdistdir}/doc/latex/comprehensive/SYMLIST
%doc %{_texmfdistdir}/doc/latex/comprehensive/source/Makefile
%doc %{_texmfdistdir}/doc/latex/comprehensive/source/lightbulb.eps
%doc %{_texmfdistdir}/doc/latex/comprehensive/source/lightbulb.map
%doc %{_texmfdistdir}/doc/latex/comprehensive/source/lightbulb.mf
%doc %{_texmfdistdir}/doc/latex/comprehensive/source/lightbulb10.mf
%doc %{_texmfdistdir}/doc/latex/comprehensive/source/lightbulb10.pfb
%doc %{_texmfdistdir}/doc/latex/comprehensive/source/makefakeMnSymbol
%doc %{_texmfdistdir}/doc/latex/comprehensive/source/response.eps
%doc %{_texmfdistdir}/doc/latex/comprehensive/source/symbols.ist
%doc %{_texmfdistdir}/doc/latex/comprehensive/source/symbols.tex
%doc %{_texmfdistdir}/doc/latex/comprehensive/source/teubner-subset.sty
%doc %{_texmfdistdir}/doc/latex/comprehensive/source/versicle.eps
%doc %{_texmfdistdir}/doc/latex/comprehensive/symbols-a4.pdf
%doc %{_texmfdistdir}/doc/latex/comprehensive/symbols-letter.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
