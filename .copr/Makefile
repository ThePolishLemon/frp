srpm:
	dnf install -y rpmdevtools rpkg golang jq sed
	#@url="https://api.github.com/repos/fatedier/frp/releases/latest"; \
	#latest_version=$$(curl -s $$url | jq -r '.tag_name' | sed 's/^v//'); \
	#sed -i "s/0\.63\.0/$$latest_version/" frp.spec; \
	spectool --get-files frp.spec
	rpmbuild -bs $(CURDIR)/frp.spec \
	--define "_topdir $(CURDIR)" \
	--define "_srcrpmdir $(outdir)"

