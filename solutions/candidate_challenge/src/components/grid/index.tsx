import { RoverPosition } from '../../pages/home';
import Cell from '../cell';

interface Grid {
  gridSize: number,
  roverPosition: RoverPosition,
  obstacles: any
}

// array(gridSize) cria um array com o tamanho especificado em gridSize
const Grid = ({ gridSize, roverPosition, obstacles }: Grid) => {
  const { x, y, direction } = roverPosition;

  const grid = Array(gridSize)
    .fill(null)
    .map((_, rowIndex) => (
      <div
        style={{ display: 'flex' }}
        key={rowIndex}
      >
        {Array(gridSize)
          .fill(null)
          .map((_, colIndex) => {
            // verifica se há obstáculo na posição (colIndex, rowIndex)
            const isObstacle = obstacles.some(
              (obstacle: any) => obstacle.x === colIndex && obstacle.y === rowIndex
            );

            return (
              <Cell
                key={colIndex}
                isRover={x === colIndex && y === rowIndex}
                isObstacle={isObstacle}
                directionData={direction}
              />
            );
          })}
      </div>
    ));

  return <div>{grid}</div>;
};


export default Grid;
