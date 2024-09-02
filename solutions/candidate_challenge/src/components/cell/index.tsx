
interface Grid {
  isRover: boolean;
  isObstacle: boolean;
  directionData: string;
}

const Cell = ({ isRover, isObstacle, directionData }: Grid) => {

  const infoDirection = (direction: any) => {
    if (direction === 'E' || direction === 'W') {
      // se a direção for 'E' (Leste), retorna '>'; se for 'W' (Oeste), retorna '<'
      return direction === 'E' ? '>' : '<';
    } else if (direction === 'N' || direction === 'S') {
      // Se a direção for 'N' (Norte), retorna '^'; se for 'S' (Sul), retorna 'v'
      return direction === 'N' ? '^' : 'v';
    }
    return '';
  }

  return (
    <div
      style={{
        width: '50px',
        height: '50px',
        border: '1px solid black',
        backgroundColor: isObstacle ? 'gray' : isRover ? 'red' : 'white',
        // cor de fundo: se for um obstáculo é cinza, se form rover é vermelho, nehum dos dois branco
      }}
    >
      {isRover && infoDirection(directionData)}
    </div>
  );
}

export default Cell;