class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old = image[sr][sc]

        if old == color:
            return image

        def fill(r, c):

            # Outside the grid
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return

            # Not the original color
            if image[r][c] != old:
                return

            image[r][c] = color

            # Up
            fill(r - 1, c)

            # Down
            fill(r + 1, c)

            # Left
            fill(r, c - 1)

            # Right
            fill(r, c + 1)

        fill(sr, sc)

        return image