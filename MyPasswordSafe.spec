Summary:	Password Safe - a password database utility
Summary(pl):	Password Safe - narzêdzie do zarz±dzania baz± danych hase³
Name:		MyPasswordSafe
Version:	20041004
Release:	0.1
License:	GPL v2
Group:		Applications/Databases
Source0:	http://www.semanticgap.com/myps/release/%{name}-%{version}.src.tgz
# Source0-md5:	58bb98d3515a166a5988d3e8bf281268
URL:		http://www.semanticgap.com/myps/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MyPasswordSafe is a straight-forward, easy-to-use password manager
that maintains compatibility with Password Safe files. MyPasswordSafe
has the following features:
- Safes are encrypted when they are stored to disk.
- Passwords never have to be seen, because they are copied to the
  clipboard.
- Random passwords can be generated.
- Window size, position, and column widths are remembered.
- Passwords remain encrypted until they need to be decrypted at the
  dialog and file levels.
- A safe can be made active so it will always be opened when
  MyPasswordSafe starts.
- Supports Unicode in the safes.

%description -l pl
MyPasswordSafe to prosty, ³atwy w u¿yciu zarz±dca hase³ utrzymuj±cy
kompatybilno¶æ z plikami Password Safe. MyPasswordSafe ma nastêpuj±ce
mo¿liwo¶ci:
- "Sejfy" z has³ami s± szyfrowane przy zapisie na dysk.
- Hase³ nie trzeba nigdy widzieæ, poniewa¿ s± kopiowane do schowka.
- Mog± byæ generowane has³a losowe.
- Mo¿na zapamiêtaæ rozmiar i po³o¿enie okna oraz szeroko¶ci kolumn.
- Has³a pozostaj± zaszyfrowane a¿ do chwili kiedy musz± byæ
  odszyfrowane na poziomie okien dialogowych i plików.
- "Sejf" mo¿e byæ uczyniony aktywnym, tak ¿e jest otwierany przy
  uruchomieniu MyPasswordSafe.
- Obs³uguje Unikod w has³ach.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin

%{__make} \
	PREFIX=/usr

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

#files
#defattr(644,root,root,755)
