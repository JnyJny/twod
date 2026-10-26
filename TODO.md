# TODO

- Point in polygon: a `Polygon` could test containment with `Point.ccw`
  over a list of points. `Point.inside` only compares against the bounds of
  two corner points.
- Point-like duck typing: accept objects with `len() == 2` and indexing, such
  as `pygame.Vector2` and numpy rows, in `Point.from_point_like`. Keep
  rejecting strings, bytes, sets and dicts. Wait for a pygame demo to show
  whether it is needed.
- Strict length: `p.xy = (1, 2, 3)` silently drops the extra value, and
  `from_point_like` raises `IndexError` for sequences shorter than two. Decide
  whether both should be a `TypeError`.
