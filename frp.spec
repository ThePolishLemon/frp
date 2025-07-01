# sed will replace these values
%global build_version 0.63.0
%global branch master
%global commit 0
%global debug_package %{nil}

Name: frp
Version: %{build_version}
Release: 1%{?dist}
Summary: unofficial spec file for frp
License: Apache-2.0
URL: https://github.com/fatedier/frp
Source: https://github.com/fatedier/frp/archive/refs/tags/v%{build_version}.tar.gz
Requires: golang


%description
FRP rpm build

%prep
%setup

%build
make build

cat <<EOF > frps.service
[Unit]
Description=FRP Server
After=network.target syslog.target
Wants=network.target

[Service]
Type=simple
ExecStart=/usr/bin/frps -c /etc/frp/frps.toml
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF


cat <<EOF > frpc.service
[Unit]
Description=FRP Client
After=network.target syslog.target
Wants=network.target
[Service]
Type=simple
ExecStart=/usr/bin/frpc -c /etc/frp/frpc.toml
Restart=on-failure
[Install]
WantedBy=multi-user.target
EOF

%check
# ensure output is correct

%install
install -D -m 0755 conf/frps.toml %{buildroot}/etc/frp/frps.toml
install -D -m 0755 conf/frpc.toml %{buildroot}/etc/frp/frpc.toml

install -D -m 0755 frps.service %{buildroot}/etc/systemd/system/frps.service
install -D -m 0755 frpc.service %{buildroot}/etc/systemd/system/frpc.service

install -D -m 0755 bin/frps %{buildroot}%{_bindir}/frps
install -D -m 0755 bin/frpc %{buildroot}%{_bindir}/frpc
%files
%{_bindir}/frps
%{_bindir}/frpc
/etc/frp/frps.toml
/etc/frp/frpc.toml

%changelog
* Tue Jul 01 2025 Unknown name 0.63.0-1
- new package built with tito


