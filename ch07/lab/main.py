import rectangle
import surface

def main():
    r1 = rectangle.Rectangle(10, 10, 10, 10)
    assert((r1.x, r1.y, r1.height, r1.width) == (10,10,10,10))
    r2 = rectangle.Rectangle(-1, 1, 1, 1)
    assert((r2.x, r2.y, r2.height, r2.width) == (1,1,1,1))
    r3 = rectangle.Rectangle(1, -5, 1, 1)
    assert((r3.x, r3.y, r3.height, r3.width) == (1,5,1,1))
    r4 = rectangle.Rectangle(1, 1, -10, 1)
    assert((r4.x, r4.y, r4.height, r4.width) == (1,1,10,1))
    r5 = rectangle.Rectangle(1, 1, 1, -1000)
    assert((r5.x, r5.y, r5.height, r5.width) == (1,1,1,1000))

    s = surface.Surface("myimage.png", 10, 10, 10, 10)
    assert((s.rect.x, s.rect.y, s.rect.height, s.rect.width) == (10,10,10,10))
    srect = s.getRect()
    assert((srect.x,  s.getRect().y, srect.height,  srect.width) == (10,10,10,10))
    assert s.image
    print("Test Complete!")

main()