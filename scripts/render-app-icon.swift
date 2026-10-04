#!/usr/bin/env swift

import CoreGraphics
import Foundation
import ImageIO
import UniformTypeIdentifiers

// Reproduces StrawberryView's native geometry on an opaque icon canvas.
// Run from the repository root: swift scripts/render-app-icon.swift
let output = URL(fileURLWithPath: CommandLine.arguments.count > 1
    ? CommandLine.arguments[1]
    : "MathBuddy/Assets.xcassets/AppIcon.appiconset/AppIcon.png")
let side = 1024
let colorSpace = CGColorSpace(name: CGColorSpace.sRGB)!
let bitmapInfo = CGImageAlphaInfo.noneSkipLast.rawValue | CGBitmapInfo.byteOrder32Big.rawValue
guard let context = CGContext(data: nil, width: side, height: side, bitsPerComponent: 8,
                              bytesPerRow: side * 4, space: colorSpace, bitmapInfo: bitmapInfo) else {
    fatalError("Could not create the icon drawing context")
}

func color(_ red: CGFloat, _ green: CGFloat, _ blue: CGFloat, alpha: CGFloat = 1) -> CGColor {
    CGColor(colorSpace: colorSpace, components: [red, green, blue, alpha])!
}

context.setFillColor(color(1, 0.976, 0.925))
context.fill(CGRect(x: 0, y: 0, width: side, height: side))
context.translateBy(x: 92, y: 932)
context.scaleBy(x: 8.4, y: -8.4)
context.setAllowsAntialiasing(true)

let berry = CGMutablePath()
berry.move(to: CGPoint(x: 50, y: 91))
berry.addCurve(to: CGPoint(x: 15, y: 39), control1: CGPoint(x: 22, y: 76), control2: CGPoint(x: 10, y: 53))
berry.addCurve(to: CGPoint(x: 50, y: 26), control1: CGPoint(x: 17, y: 23), control2: CGPoint(x: 33, y: 19))
berry.addCurve(to: CGPoint(x: 85, y: 39), control1: CGPoint(x: 69, y: 18), control2: CGPoint(x: 85, y: 22))
berry.addCurve(to: CGPoint(x: 50, y: 91), control1: CGPoint(x: 92, y: 56), control2: CGPoint(x: 70, y: 83))
berry.closeSubpath()
context.addPath(berry)
context.setFillColor(color(0.851, 0.365, 0.278))
context.fillPath()

let highlight = CGMutablePath()
highlight.move(to: CGPoint(x: 28, y: 37))
highlight.addQuadCurve(to: CGPoint(x: 39, y: 74), control: CGPoint(x: 18, y: 53))
context.addPath(highlight)
context.setStrokeColor(color(1, 1, 1, alpha: 0.2))
context.setLineWidth(6)
context.setLineCap(.round)
context.strokePath()

let seeds: [CGPoint] = [
    .init(x: 39, y: 43), .init(x: 60, y: 41), .init(x: 29, y: 53),
    .init(x: 51, y: 58), .init(x: 70, y: 55), .init(x: 42, y: 73), .init(x: 62, y: 70)
]
context.setFillColor(color(0.965, 0.849, 0.533))
for seed in seeds {
    context.fillEllipse(in: CGRect(x: seed.x - 1.6, y: seed.y - 3, width: 3.2, height: 6))
}

let leaves = CGMutablePath()
leaves.addLines(between: [
    .init(x: 49, y: 29), .init(x: 21, y: 20), .init(x: 36, y: 36),
    .init(x: 51, y: 29), .init(x: 69, y: 34), .init(x: 80, y: 18),
    .init(x: 58, y: 25), .init(x: 56, y: 9), .init(x: 46, y: 24), .init(x: 36, y: 12)
])
leaves.closeSubpath()
context.addPath(leaves)
context.setFillColor(color(0.137, 0.302, 0.224))
context.fillPath()

guard let image = context.makeImage() else { fatalError("Could not render the icon") }
try FileManager.default.createDirectory(at: output.deletingLastPathComponent(), withIntermediateDirectories: true)
guard let destination = CGImageDestinationCreateWithURL(output as CFURL, UTType.png.identifier as CFString, 1, nil) else {
    fatalError("Could not create the PNG output")
}
CGImageDestinationAddImage(destination, image, nil)
guard CGImageDestinationFinalize(destination) else { fatalError("Could not write the PNG") }
print("Rendered opaque 1024 × 1024 app icon to \(output.path)")
