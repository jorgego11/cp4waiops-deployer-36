echo ""
echo "*****************************************************************************************************************************"
echo " 🐥 Turbonomic - Event Driven Ansible"
echo "*****************************************************************************************************************************"
echo "  "
echo ""
echo ""

#export INSTALL_REPO=https://github.com/niklaushirt/aiops-install-awx-33.git

echo "   ------------------------------------------------------------------------------------------------------------------------------"
echo "   🌏  Get EDA from $EDA_REPO"
git clone $EDA_REPO eda | sed 's/^/      /'
cd eda
pwd| sed 's/^/         /'

echo "   ------------------------------------------------------------------------------------------------------------------------------"
echo "   🔎  Available Rulebooks"
ls -al playbooks| sed 's/^/         /'

echo "   ------------------------------------------------------------------------------------------------------------------------------"
echo "   🔎  Available Playbooks"
ls -al playbooks| sed 's/^/         /'

echo "  "
echo ""
echo ""
echo "  "
echo ""
echo ""
echo "*****************************************************************************************************************************"
echo "🚀  Starting EDA Server"
echo "*****************************************************************************************************************************"
echo "  "
echo ""
echo ""

./start-eda.sh


echo "*****************************************************************************************************************************"
echo " ✅ DONE"
echo "*****************************************************************************************************************************"


