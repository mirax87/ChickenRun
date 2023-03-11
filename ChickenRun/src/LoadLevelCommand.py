import pytmx
import os

from pygame import Vector2

class LoadLevelCommand:

    def __init__(self, gameMode, fileName):
        self.gameMode = gameMode
        self.fileName = fileName

    def run(self):
        if not os.path.exists(self.fileName):
            raise RuntimeError("No file {}".format(self.fileName))
        tileMap = tmx.TileMap.load(self.fileName)

        if tileMap.orientation != "orthogonal":
            raise RuntimeError("Error in {}: invalid orientation".format(self.fileName))

        # if len(tileMap.layers) != 5:
        #     raise RuntimeError("Error in {}: 5 layers are expected".format(self.fileName))

        state = self.gameMode.gameState
        state.worldSize = Vector2(tileMap.width, tileMap.height)    

        # decode layer0
        tileset, array = self.decodeArrayLayer(tileMap, tileMap.layers[0])
        cellSize = Vector2(tileset.tilewidth, tileset.tileheight)
        state.ground[:] = array
        imageFile = tileset.image.source
        self.gameMode.layers[0].setTileset(cellSize, imageFile)

    def decodeArrayLayer(self, tileMap, layer):
        tileset = self.decodeLayer(tileMap, layer)

        array = [None] * tileMap.height
        for y in range(tileMap.height):
            array[y] = [None] * tileMap.width
            for x in range(tileMap.width):
                tile = layer.tiles[x + y*tileMap.width]
                if tile.gid == 0:
                    continue
                lid = tile.gid - tileset.firstgid
                if lid < 0 or lid >= tileset.tilecount:
                    raise RuntimeError("Error in {}: invalid tile id".format(self.fileName))
                tileX = lid % tileset.columns
                tileY = lid // tileset.columns
                array[y][x] = Vector2(tileX, tileY)

        return tileset, array
    

    def decodeLayer(self, tileMap, layer):
        if not isinstance(layer, tmx.Layer):
            raise RuntimeError("Error in {}: invalid layer type".format(self.fileName))
        if len(layer.tiles) != tileMap.width * tileMap.height:
            raise RuntimeError("Error in {}: invalid tiles count".format(self.fileName))

        # Guess which tileset is used by this layer
        gid = None
        for tile in layer.tiles:
            if tile.gid != 0:
                gid = tile.gid
                break
            if gid is None:
                if len(tileMap.tilesets) == 0:
                    raise RuntimeError("Error in {}: no tilesets".format(self.fileName))
                tileset = tileMap.tilesets[0]
            else:
                tileset = None
                for t in tileMap.tilesets:
                    if gid >= t.firstgid and gid < t.firstgid+t.tilecount:
                        tileset = t
                        break
                if tileset is None:
                    raise RuntimeError("Error in {}: no corresponding tileset".format(self.fileName))

        # Check the tileset
        if tileset.columns <= 0:
            raise RuntimeError("Error in {}: invalid columns count".format(self.fileName))
        if tileset.image.data is not None:
            raise RuntimeError("Error in {}: embedded tileset image is not supported".format(self.fileName))

        return tileset