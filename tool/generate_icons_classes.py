# This script must be run from the root of the project

import os


def folderNameToPascalCase(string):
    return ''.join(x.capitalize() for x in string.split('_'))


def fileNameToCamelCase(string):
    return string.split('.')[0].split('-')[0] + ''.join(x.capitalize() for x in string.split('.')[0].split('-')[1:])


def createClassHeader(className, prefixWithUntitled=True):
    if prefixWithUntitled:
        return f'abstract class Untitled{className} {{\n'
    else:
        return f'abstract class {className} {{\n'


def createClassFooter():
    return '}'


def createIconEntry(iconFile, iconsFolder):
    fileNameWithoutExtension = iconFile.split('.')[0]
    camelFileName = fileNameToCamelCase(fileNameWithoutExtension)
    variableDeclaration = '\tstatic const ' + camelFileName
    variableValue = f"'assets/{iconsFolder}/{iconFile}'" + ';\n'
    return variableDeclaration + ' = ' + variableValue


def createBarrelExportEntry(iconsFolder):
    return f"export '{iconsFolder}.dart';\n"


def main():
    cwd = os.getcwd()
    assetsFolder = os.path.join(cwd, 'assets')
    iconsClassesFolder = os.path.join(cwd, 'lib', 'src', 'icons')

    allIconsClassFile = open(os.path.join(
        iconsClassesFolder, 'untitled_icons.dart'), 'w')
    allIconsClassFile.write(createClassHeader(
        'UntitledIcons', prefixWithUntitled=False))

    barrelFile = open(os.path.join(iconsClassesFolder, 'icons.dart'), 'w')
    barrelFile.write(createBarrelExportEntry('untitled_icons'))

    iconsFolders = os.listdir(assetsFolder)

    for iconsFolder in iconsFolders:
        barrelFile.write(createBarrelExportEntry(iconsFolder))
        iconsClassPath = os.path.join(
            iconsClassesFolder, iconsFolder + '.dart')
        file = open(iconsClassPath, 'w')

        pascalFolderName = folderNameToPascalCase(iconsFolder)
        file.write(createClassHeader(pascalFolderName))

        iconsFiles = os.listdir(os.path.join(assetsFolder, iconsFolder))

        for iconFile in iconsFiles:
            file.write(createIconEntry(iconFile, iconsFolder))
            allIconsClassFile.write(createIconEntry(iconFile, iconsFolder))

        file.write(createClassFooter())

    allIconsClassFile.write(createClassFooter())

    os.system(f'dart format {iconsClassesFolder}')


if __name__ == "__main__":
    main()
