import SwiftUI

/// Native, independently animated mathematical objects stay crisp at any iPad scale.
struct StrawberryView: View {
    var body: some View {
        Canvas { context, size in
            let sx = size.width / 100
            let sy = size.height / 100
            var berry = Path()
            berry.move(to: CGPoint(x: 50 * sx, y: 91 * sy))
            berry.addCurve(to: CGPoint(x: 15 * sx, y: 39 * sy), control1: CGPoint(x: 22 * sx, y: 76 * sy), control2: CGPoint(x: 10 * sx, y: 53 * sy))
            berry.addCurve(to: CGPoint(x: 50 * sx, y: 26 * sy), control1: CGPoint(x: 17 * sx, y: 23 * sy), control2: CGPoint(x: 33 * sx, y: 19 * sy))
            berry.addCurve(to: CGPoint(x: 85 * sx, y: 39 * sy), control1: CGPoint(x: 69 * sx, y: 18 * sy), control2: CGPoint(x: 85 * sx, y: 22 * sy))
            berry.addCurve(to: CGPoint(x: 50 * sx, y: 91 * sy), control1: CGPoint(x: 92 * sx, y: 56 * sy), control2: CGPoint(x: 70 * sx, y: 83 * sy))
            context.fill(berry, with: .color(Storybook.coral))
            var highlight = Path()
            highlight.move(to: CGPoint(x: 28 * sx, y: 37 * sy))
            highlight.addQuadCurve(to: CGPoint(x: 39 * sx, y: 74 * sy), control: CGPoint(x: 18 * sx, y: 53 * sy))
            context.stroke(highlight, with: .color(.white.opacity(0.2)), style: StrokeStyle(lineWidth: 6 * sx, lineCap: .round))
            let seeds: [CGPoint] = [.init(x: 39, y: 43), .init(x: 60, y: 41), .init(x: 29, y: 53), .init(x: 51, y: 58), .init(x: 70, y: 55), .init(x: 42, y: 73), .init(x: 62, y: 70)]
            for seed in seeds {
                let rect = CGRect(x: (seed.x - 1.6) * sx, y: (seed.y - 3) * sy, width: 3.2 * sx, height: 6 * sy)
                context.fill(Path(ellipseIn: rect), with: .color(Storybook.butter))
            }
            var leaves = Path()
            let points = [CGPoint(x: 49, y: 29), CGPoint(x: 21, y: 20), CGPoint(x: 36, y: 36), CGPoint(x: 51, y: 29), CGPoint(x: 69, y: 34), CGPoint(x: 80, y: 18), CGPoint(x: 58, y: 25), CGPoint(x: 56, y: 9), CGPoint(x: 46, y: 24), CGPoint(x: 36, y: 12)]
            leaves.addLines(points.map { CGPoint(x: $0.x * sx, y: $0.y * sy) })
            leaves.closeSubpath()
            context.fill(leaves, with: .color(Storybook.forest))
        }
        .aspectRatio(1, contentMode: .fit)
        .accessibilityHidden(true)
    }
}

struct BasketView: View {
    var body: some View {
        Canvas { context, size in
            let w = size.width
            let h = size.height
            var handle = Path()
            handle.addArc(center: CGPoint(x: w * 0.5, y: h * 0.41), radius: w * 0.32, startAngle: .degrees(180), endAngle: .degrees(0), clockwise: false)
            context.stroke(handle, with: .color(Storybook.wood), style: StrokeStyle(lineWidth: 10, lineCap: .round))
            var basket = Path()
            basket.move(to: CGPoint(x: w * 0.1, y: h * 0.4))
            basket.addLine(to: CGPoint(x: w * 0.9, y: h * 0.4))
            basket.addLine(to: CGPoint(x: w * 0.8, y: h * 0.93))
            basket.addQuadCurve(to: CGPoint(x: w * 0.2, y: h * 0.93), control: CGPoint(x: w * 0.5, y: h))
            basket.closeSubpath()
            context.fill(basket, with: .color(Storybook.wood))
            var weave = Path()
            for ratio in [0.27, 0.42, 0.58, 0.73] {
                weave.move(to: CGPoint(x: w * ratio, y: h * 0.46))
                weave.addLine(to: CGPoint(x: w * (0.5 + (ratio - 0.5) * 0.76), y: h * 0.91))
            }
            for ratio in [0.54, 0.69, 0.83] {
                weave.move(to: CGPoint(x: w * 0.2, y: h * ratio))
                weave.addLine(to: CGPoint(x: w * 0.8, y: h * ratio))
            }
            context.stroke(weave, with: .color(Storybook.butter.opacity(0.63)), lineWidth: 5)
            context.fill(Path(roundedRect: CGRect(x: w * 0.06, y: h * 0.38, width: w * 0.88, height: h * 0.09), cornerRadius: 5), with: .color(Color(red: 0.84, green: 0.64, blue: 0.39)))
        }
        .accessibilityHidden(true)
    }
}

struct PinwheelView: View {
    var rotation = 0.0

    var body: some View {
        GeometryReader { proxy in
            let diameter = min(proxy.size.width, proxy.size.height * 0.62)
            ZStack(alignment: .top) {
                RoundedRectangle(cornerRadius: 5)
                    .fill(Storybook.wood)
                    .frame(width: 9, height: proxy.size.height * 0.78)
                    .offset(y: diameter * 0.34)
                Canvas { context, size in
                    let center = CGPoint(x: size.width / 2, y: size.height / 2)
                    let colors = [Storybook.coral, Storybook.butter, Storybook.forest, Storybook.sky]
                    for index in 0..<4 {
                        var rotated = context
                        rotated.translateBy(x: center.x, y: center.y)
                        rotated.rotate(by: .degrees(Double(index) * 90))
                        var blade = Path()
                        blade.move(to: .zero)
                        blade.addLine(to: CGPoint(x: -size.width * 0.46, y: -size.height * 0.42))
                        blade.addQuadCurve(to: CGPoint(x: size.width * 0.06, y: -size.height * 0.45), control: CGPoint(x: -size.width * 0.08, y: -size.height * 0.54))
                        blade.closeSubpath()
                        rotated.fill(blade, with: .color(colors[index]))
                    }
                    context.fill(Path(ellipseIn: CGRect(x: center.x - 8, y: center.y - 8, width: 16, height: 16)), with: .color(Storybook.paper))
                }
                .frame(width: diameter, height: diameter)
                .rotationEffect(.degrees(rotation))
            }
            .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .top)
        }
        .accessibilityHidden(true)
    }
}

struct LittleFlower: View {
    var color = Storybook.coral
    var body: some View {
        ZStack {
            ForEach(0..<5, id: \.self) { petal in
                Ellipse()
                    .fill(color)
                    .frame(width: 16, height: 26)
                    .offset(y: -12)
                    .rotationEffect(.degrees(Double(petal) * 72))
            }
            Circle().fill(Storybook.butter).frame(width: 13, height: 13)
        }
        .frame(width: 52, height: 52)
        .accessibilityHidden(true)
    }
}
