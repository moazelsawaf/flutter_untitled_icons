import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:vector_graphics/vector_graphics.dart';

const _untitledPrimaryColor = Color(0xFF6941C6);
const _packageName = 'untitled_icons';

class UntitledIcon extends StatelessWidget {
  final String icon;
  final double size;
  final Color color;
  final String? packageName;
  final bool customIcon;

  const UntitledIcon({
    super.key,
    required this.icon,
    this.size = 24,
    this.color = _untitledPrimaryColor,
    this.packageName,
    this.customIcon = false,
  });

  @override
  Widget build(BuildContext context) {
    final packageNameString = packageName ?? (customIcon ? null : _packageName);
    return SvgPicture(
      icon.endsWith('.vec')
          ? AssetBytesLoader(icon, packageName: packageNameString)
          : SvgAssetLoader(icon, packageName: packageNameString),
      height: size,
      width: size,
      colorFilter: ColorFilter.mode(color, BlendMode.srcIn),
    );
  }
}
