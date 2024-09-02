import { useState } from 'react';
import Grid from '../../components/grid';
import {
  ArrowLeftIcon,
  ArrowPathRoundedSquareIcon,
  ArrowRightIcon,
  PlusCircleIcon
} from '@heroicons/react/24/solid';

export interface RoverPosition {
  x: number,
  y: number,
  direction: string
}

const initialPosition = {
  x: 0,
  y: 0,
  direction: 'E'
};

const RoverController = () => {
    const gridSize = 5; // tamanho da grade como 5x5.
    const [roverPosition, setRoverPosition] = useState<RoverPosition>(initialPosition);
    const [collectInfo, setCollectInfo] = useState<string>('');

    // array que define as posições dos obstáculos na grade
    const obstacles = [
      { x: 2, y: 2 },
      { x: 3, y: 1 }
    ];

    // função para coletar informações na posição atual do rover
    const headlerCollect = () => {
      setCollectInfo(`${roverPosition?.x}, ${roverPosition?.y}`);
    }

     // verificar se a próxima posição está ocupada por um obstáculo
    const isObstacle = (nextX: number, nextY: number) => {
      return obstacles.some(
        (obstacle: any) => obstacle?.x === nextX && obstacle?.y === nextY
      );
    };

    // função para mover o rover de acordo com o comando fornecido
    const moveRover = (command: string) => {
      setRoverPosition((prevPosition) => {
        let { x, y, direction } = prevPosition;

        // Muda a posição ou direção do rover com base no comando recebido
        switch (command) {
          case 'F': // Avançar
            if (direction === 'N' && y > 0 && !isObstacle(x, y - 1)) {
              y -= 1;
            }
            if (direction === 'S' && y < gridSize - 1 && !isObstacle(x, y + 1)) {
              y += 1;
            }
            if (direction === 'E' && x < gridSize - 1 && !isObstacle(x + 1, y)) {
              x += 1;
            }
            if (direction === 'W' && x > 0 && !isObstacle(x - 1, y)) {
              x -= 1;
            }
            break;
          case 'B': // Voltar
            if (direction === 'N' && y < gridSize - 1 && !isObstacle(x, y + 1)) {
              y += 1;
            }
            if (direction === 'S' && y > 0 && !isObstacle(x, y - 1)) {
              y -= 1;
            }
            if (direction === 'E' && x > 0 && !isObstacle(x - 1, y)) {
              x -= 1;
            }
            if (direction === 'W' && x < gridSize - 1 && !isObstacle(x + 1, y)) {
              x += 1;
            }
            break;
          case 'L': // Girar anti-horário
            if (direction === 'N') {
              direction = 'W';
            } else if (direction === 'W') {
              direction = 'S';
            } else if (direction === 'S') {
              direction = 'E';
            } else if (direction === 'E') {
              direction = 'N';
            }
            break;
          case 'R': // Girr horário
            if (direction === 'N') {
              direction = 'E';
            } else if (direction === 'E') {
              direction = 'S';
            } else if (direction === 'S') {
              direction = 'W';
            } else if (direction === 'W') {
              direction = 'N';
            }
            break;
          default:
            break;
        }

        return { x, y, direction };
      });
    };

    return (
      <div className="flex items-center justify-center h-screen">
          <div className="bg-white shadow-lg rounded-lg p-6 w-full max-w-md">
              <div className="text-center mb-4">
                  <h1 className="text-4xl font-bold">Sistema de Controle em Marte</h1>
              </div>
              <div className="flex justify-center mb-4">
                  <Grid
                      gridSize={gridSize}
                      roverPosition={roverPosition}
                      obstacles={obstacles}
                  />
              </div>
              <div className="mt-4 flex justify-center space-x-2">
                  <button
                    className="flex text-sm items-center bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-700"
                    onClick={() => moveRover('F')}
                    title='Avançar'
                  >
                    Avançar
                    <ArrowRightIcon className="w-5 h-5 ml-2" />
                  </button>
                  <button
                    className="flex text-sm items-center bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-700"
                    onClick={() => moveRover('B')}
                    title='Voltar'
                  >
                    Voltar
                    <ArrowLeftIcon className="w-5 h-5 ml-2" />
                  </button>
              </div>
              <div className="mt-4 flex justify-center space-x-2">
                  <button
                    className="flex text-xs items-center bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-700"
                    onClick={() => moveRover('L')}
                  >
                    Girar anti-horário
                    <ArrowPathRoundedSquareIcon className="w-5 h-5 ml-2" />
                  </button>
                  <button
                    className="flex text-xs items-center bg-blue-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-700"
                    onClick={() => moveRover('R')}
                  >
                    Girar horário
                    <ArrowPathRoundedSquareIcon className="w-5 h-5 ml-2" />
                  </button>
              </div>
              <div className="mt-4 flex justify-center space-x-2">
                  <button
                  className="flex items-center bg-green-500 text-white font-bold py-2 px-4 rounded hover:bg-blue-700"
                  onClick={headlerCollect}
                  >
                    Coletar
                    <PlusCircleIcon className="w-5 h-5 ml-2" />
                  </button>
              </div>
              {collectInfo && (
                  <div className="mt-4 text-center bg-yellow-600 text-white font-bold py-2 px-4 rounded-full">
                      Coletado: {collectInfo}
                  </div>
              )}
          </div>
      </div>
  );
}

export default RoverController;
