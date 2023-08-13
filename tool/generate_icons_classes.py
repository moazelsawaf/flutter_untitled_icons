# This script must be run from the root of the project

import os


def folderNameToPascalCase(string):
    return ''.join(x.capitalize() for x in string.split('_'))


def fileNameToCamelCase(string):
    return string.split('.')[0].split('-')[0] + ''.join(x.capitalize() for x in string.split('.')[0].split('-')[1:])


cwd = os.getcwd()
assetsFolder = os.path.join(cwd, 'assets')

barrelFile = open(os.path.join(cwd, 'lib', 'src', 'icons', 'icons.dart'), 'w')

iconsFolders = os.listdir(assetsFolder)

for iconsFolder in iconsFolders:
    barrelFile.write(f"export '{iconsFolder}.dart';\n")
    iconsClassPath = os.path.join(
        cwd, 'lib', 'src', 'icons', iconsFolder + '.dart')
    file = open(iconsClassPath, 'w')

    pascalFolderName = folderNameToPascalCase(iconsFolder)
    file.write('abstract class ' + pascalFolderName + ' {\n')

    iconsFiles = os.listdir(os.path.join(assetsFolder, iconsFolder))

    for iconFile in iconsFiles:
        fileNameWithoutExtension = iconFile.split('.')[0]
        camelFileName = fileNameToCamelCase(fileNameWithoutExtension)
        variableDeclaration = '\tstatic const ' + camelFileName
        variableValue = f"'assets/{iconsFolder}/{iconFile}'" + ';\n'
        file.write(variableDeclaration + ' = ' + variableValue)

    file.write('}')


os.system('dart format lib/src/icons')
