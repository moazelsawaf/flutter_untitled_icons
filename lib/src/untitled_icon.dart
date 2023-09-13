import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:vector_graphics/vector_graphics.dart';

const _untitledPrimaryColor = Color(0xFF6941C6);
const _packageName = 'untitled_icons';

class UntitledIcon extends StatelessWidget {
  final String icon;
  final double size;
  final Color color;
  final bool _isCustomSvg;

  const UntitledIcon({
    super.key,
    required this.icon,
    this.size = 24,
    this.color = _untitledPrimaryColor,
  }) : _isCustomSvg = false;

  const UntitledIcon.customSvg({
    super.key,
    required this.icon,
    this.size = 24,
    this.color = _untitledPrimaryColor,
  }) : _isCustomSvg = true;

  @override
  Widget build(BuildContext context) {
    return SvgPicture(
      _isCustomSvg
          ? SvgAssetLoader(icon)
          : AssetBytesLoader(icon, packageName: _packageName),
      height: size,
      width: size,
      colorFilter: ColorFilter.mode(color, BlendMode.srcIn),
    );
  }
}
