#!/bin/bash
RED="\e[1;31m"
GREEN="\e[1;32m"
NC="\e[0m"

# Prevent wrong usage
if [[ $(uname) != Linux ]]
then
    echo -e "${RED}Error${NC}: ZenMaxBuilder is for Linux..."
    exit 1
elif [ ! -f ZenMaxBuilder.py ] || [ ! -d modules ]
then
    echo -e "${RED}Error${NC}: run installer from ZenMaxBuilder folder..."
    exit 1
fi

# Set the package manager of the current Linux distribution
declare -A PMS=(
    [aarch64]="_ apt-get update install -y"
    [redhat]="sudo yum update install -y"
    [arch]="sudo pacman -Syu -s --noconfirm"
    [gentoo]="sudo emerge --update -1 -y"
    [suse]="sudo zypper update install -y"
    [fedora]="sudo dnf update install -y"
)
OS=(aarch64 redhat arch gentoo suse fedora)
for DIST in "${OS[@]}"
do
    case ${DIST} in "aarch64") ARG="-m";; *) ARG="-v"; esac
    if uname ${ARG} | grep -qi "${DIST}"
    then
        IFS=" "
        PM=${PMS[${DIST}]}
        read -ra PM <<< "$PM"
        break
    else
        PM=(sudo apt-get update install -y)
    fi
done

# Check command status and exit on error
check() {
    "${@}"
    local STATUS=$?
    if [[ ${STATUS} -ne 0 ]]
    then
        echo -e "${RED}Error${NC}: ${*}"
        exit 1
    fi
    return "${STATUS}"
}

# Update system
echo -e "\n${GREEN}Updating system...${NC}"
check eval "${PM[0]//_/} ${PM[1]} ${PM[2]} ${PM[4]}"

# Install missing dependencies
DEPENDENCIES=(wget git zip llvm lld make automake python)
for PACKAGE in "${DEPENDENCIES[@]}"
do
    if ! which "${PACKAGE//llvm/llvm-ar}" &>/dev/null
    then
        echo -e \
            "\n${RED}Package ${PACKAGE} not found. ${GREEN}Installing...${NC}"
        check eval "${PM[0]//_/} ${PM[1]} ${PM[3]} ${PM[4]} ${PACKAGE}"
    fi
done

# Install python requirements
echo -e "\n${GREEN}Installing python requirements...${NC}"
check pip install -r requirements.txt
if [[ $(uname -m) == aarch64 ]]
then
    check pip install termcolor requests
fi

# Create ZenMaxBuilder alias (for bash and zsh only)
ENV=(.bashrc .zshrc)
for FILE in "${ENV[@]}"
do
    if [[ -f ${HOME}/${FILE} ]] && \
            ! grep "alias ZenMaxBuilder=" "${HOME}/${FILE}" &>/dev/null
    then
        echo -e "\n${GREEN}Creating ZenMaxBuilder alias for ${FILE}...${NC}"
        printf "\n# ZenMaxBuilder\nalias zmb='cd %s && python3 zmb.py'" \
            "$PWD" >> "${HOME}/${FILE}"
        echo -e "Successfully created."
    fi
done
echo -e "\n${RED}Exiting...${NC}"
kill -9 $$ ${BASHPID}
exec ${SHELL}
