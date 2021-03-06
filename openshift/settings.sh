export PROJECT_NAMESPACE="nbup6o"
export PROJECT_OS_DIR=${PROJECT_OS_DIR:-../../openshift}

# The templates that should not have their GIT referances(uri and ref) over-ridden
# Templates NOT in this list will have they GIT referances over-ridden
# with the values of GIT_URI and GIT_REF
export skip_git_overrides="schema-spy-build.json backup-build.json"
export GIT_URI="https://github.com/bcgov/agri-dcbr.git"
export GIT_REF="master"

# The project components
export components="dcbr-db dcbr-api dcbr-web dcbr-backup weasyprint"

# The builds to be triggered after buildconfigs created (not auto-triggered)
export builds=""

# The images to be tagged after build
export images="dcbr-db dcbr-api dcbr-web schema-spy"

# The routes for the project
export routes="dcbr-db dcbr-api dcbr-web schema-spy"
