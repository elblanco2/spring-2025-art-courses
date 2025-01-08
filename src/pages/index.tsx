import Week1Page from '../modules/ART1201C/weeks/Week1';
import Week2Page from '../modules/ART1201C/weeks/Week2';
import Week3Page from '../modules/ART1201C/weeks/Week3';

export default function Home() {
  return (
    <main className="min-h-screen p-8">
      <div className="space-y-8">
        <Week1Page />
        <Week2Page />
        <Week3Page />
      </div>
    </main>
  );
}